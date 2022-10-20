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
    #date = re.sub(r"\D","",date)
    date_obj = datetime.strptime(date,'%Y%m%d')
    date = datetime.strftime(date_obj,'%Y-%m-%d')
    transcript = comic.find(class_='transcript-content')
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
  
  return title, date, url, transcript_txt.strip()

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

def persist(db_file, pages):
  print("persisting to database")
  conn = sqlite3.connect(db_file)
  conn.row_factory = sqlite3.Row
  cursor = conn.cursor()
  sql_stmt = ("INSERT OR REPLACE INTO comic (page,title,date,url,transcript) "
              "VALUES (:page,:title,:date,:url,:transcript)")
  cursor.executemany(sql_stmt,pages)
  
  conn.commit()
  conn.close()
  return

def proc_opts():
  parser = argparse.ArgumentParser(description='Page updater')
  parser.add_argument('db',help="Database file")
  parser.add_argument('page', type=int,help="Page to update")
  parser.add_argument('--start-page',type=int, help="Start page",default=0)
  return parser.parse_args()

if __name__ == "__main__":
  args =proc_opts()

  if args.start_page > 0:
    pages = range(args.start_page,args.page)
  else:
    pages = [args.page]

  from pprint import pprint
  datum = []
  for p in pages:
    page = request_page(p)
    title,date,url,txn = parse_page(page)
    page_dic = {"page":p,'title':title,'date':date,'url':url,'transcript':txn}
    pprint(page_dic)
    datum.append(page_dic)

  persist(args.db,datum)


