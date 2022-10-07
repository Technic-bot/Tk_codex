import sqlite3
from flask import Flask, request

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['DATABASE'] = app.root_path + "/db/" +app.config['DB_NAME']

def get_db_connection(db_file):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/test")
def test_api():
  conn = get_db_connection(app.config['DATABASE'])
  res = conn.execute('Select count(*) from twokinds_comic').fetchone()
  conn.close()
  return {"Records": res[0]} 

@app.route("/text")
def text_search():
  conn = get_db_connection(app.config['DATABASE'])
  res = conn.execute('Select count(*) from twokinds_chars').fetchone()
  conn.close()
  print(res[0])
  return {"Hello": "World"} 

@app.route("/art",methods=['POST'])
def char_post():
  print("hola")
  data = request.json
  print(data)
  return data

@app.route("/art",methods=['GET'])
def char_get():
  args = request.args
  response = {} 
  characters = args.get('characters').split()
  if not characters: 
    return {"pages": []}, 404
  r = char_search(characters)
  return r

def char_search(characters):
  """Query DB for pages"""
  # Not sure if group by and having is the correct method
  question_marks = ','.join('?'*len(characters))
  sql_stmt = ('SELECT comic.page,comic.url, count(*) n FROM chars'
              ' INNER JOIN comic ON'
              ' comic.page = chars.page'
              ' WHERE CHARACTER IN ({}) group by comic.page having n == {};')
  prep_sql_stmt=sql_stmt.format(question_marks,len(characters)) 
  print(prep_sql_stmt)
  conn = get_db_connection(app.config['DATABASE'])
  rows = conn.execute(prep_sql_stmt,characters).fetchall()
  conn.close()
  print("Getting all pages with {}".format(characters))

  response = []
  for r in rows:
    page_dic = {'page':r['page'],
                'url': r['url']}
    response.append(page_dic)

  return response 
