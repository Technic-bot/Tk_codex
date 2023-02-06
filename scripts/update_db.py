import requests
from bs4 import BeautifulSoup

import sys
import argparse
from datetime import datetime
import time

import random
import os
import csv
import re

import sqlite3

end_point = "http://twokinds.keenspot.com/comic/{}/"
date_regex = re.compile(r"\d{8}")

def parse_page(page):
  try:
    sopa = BeautifulSoup(page, 'html.parser')
    comic = sopa.find(class_='comic')
    image = comic.img
    url = image['src']
    title = comic.header.h1.text
    date = os.path.basename(url)
    date = os.path.splitext(date)[0]
    result = date_regex.match(date)
    date = result.group()
    date = re.sub(r"\D","",date)
    date_obj = datetime.strptime(date,'%Y%m%d')
    date = datetime.strftime(date_obj,'%Y-%m-%d')
    transcript = comic.find(class_='transcript-content')

    permalink = sopa.find(class_="permalink")
    page = get_page_number(permalink)
    if transcript:
      transcript_txt = transcript.text
      transcript_txt = re.sub(r"Page transcript .*",'',transcript_txt)
    else:
      transcript_txt=""
  except Exception as e:
    print("Parsing error")
    print("URL: {}".format(url))
    print(e)
    transcript_txt = ""
    date = ""
    url = ""
    title = ""
    page = None
  
  return title, date, url, transcript_txt.strip(), page

def get_page_number(permalink):
    hrefs = permalink.find_all("a")
    page = None
    for h in hrefs: 
      if h.text == "Permalink":
        page = h['href'].split("/")[2]

    print(page)
    return page


def request_page(page_num):
  """ Request a comic page"""
  print('Requesting page {}'.format(page_num))
  min_j, max_j = 0 ,2 
  jitter = random.uniform(min_j,max_j)
  time.sleep(jitter)

  page_url = end_point.format(page_num)
  r = requests.get(page_url)
  r.encoding = 'utf-8'
  return r.text


def get_chars(pages):
  # Aint it fun to define nested functions?
  def _is_character(c): 
    return ":" in  c
    
  char_list = []
  for p in pages:
    txn =p['transcript']
    txn_list = txn.split()
    p_chars = set(filter(_is_character,txn_list))
    page_char_lst = [ (p['page'],x.strip(':')) for x in p_chars]
    char_list.extend(page_char_lst)
  
  #print(char_list)
  return char_list


def persist(db_file, pages):
  print("Persisting to database")
  conn = sqlite3.connect(db_file)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  sql_stmt = ("INSERT OR REPLACE INTO comic (page,title,date,url,transcript) "
              "VALUES (:page,:title,:date,:url,:transcript);")
  cursor.executemany(sql_stmt,pages)
  
  conn.commit()
  conn.close()
  return

def persist_chars(db_file,chars):
  print("Persisting character data to database")
  conn = sqlite3.connect(db_file)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  sql_stmt = ("INSERT OR REPLACE INTO chars (page,character) "
              "VALUES (?,?);")
  cursor.executemany(sql_stmt,chars)
  
  conn.commit()
  conn.close()
  
def deduplicate(db_file):
  print("Removing duplicates")
  conn = sqlite3.connect(db_file)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  # De duplicate char table
  sql_stmt = ("delete from chars where rowid not in " 
             "(select  min(rowid) from chars group by page,character);")
  cursor.execute(sql_stmt)
  # Deduplicate script
  sql_stmt = ("delete from script where rowid not in " 
             "(select  min(rowid) from script group by page,dialogue,speaker);")
  cursor.execute(sql_stmt)
  conn.commit()
  conn.close()

def make_script(pages):
  script = []
  for p in pages:
    lines = p['transcript'].split('\n')
    for line in lines:
      try:
        char,dial = line.split(':')
      except ValueError as e:
        print("Error: {}".format(line))

      line_dic = { 'speaker': char,
                    'dialogue' : dial,
                    'page': p['page'] }
      script.append(line_dic)

  return script

def persist_script(db_file,script):
  print("Persisting Script to database")
  conn = sqlite3.connect(db_file)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  sql_stmt = ("INSERT OR REPLACE INTO script (page,dialogue,speaker) "
              "VALUES (:page,:dialogue,:speaker);")
  cursor.executemany(sql_stmt,script)
  
  conn.commit()
  conn.close()
  return

def proc_opts():
  parser = argparse.ArgumentParser(description='Page updater')
  parser.add_argument('db',help="Database file")
  parser.add_argument('page', type=int,help="Page to update",default=0)
  parser.add_argument('--start-page',type=int, help="Start page",default=0)
  return parser.parse_args()

if __name__ == "__main__":
  args =proc_opts()

  if not args.page:
    print("Doing latest page")
    pages = [""]
  elif args.start_page > 0:
    # Needs the extra 1 to be inclusive
    pages = range(args.start_page,args.page+1) 
  else: 
    pages = [args.page]

  from pprint import pprint
  datum = []
  for p in pages:
    html_page = request_page(p)
    title,date,url,txn,parsed_page = parse_page(html_page)
    page_no = p
    if title:
      if not page_no:
        # No page passed try to use parsed page
        page_no = parsed_page
      page_dic = {"page":page_no,'title':title,'date':date,'url':url,'transcript':txn}
      datum.append(page_dic)

  #print(datum)
  if not datum:
    print("Nothing parsed")

  persist(args.db,datum)

  chrs = get_chars(datum)
  persist_chars(args.db,chrs)

  scrpt = make_script(datum)  
  persist_script(args.db,scrpt)

  deduplicate(args.db)


