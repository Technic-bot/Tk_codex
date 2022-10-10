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
  res = conn.execute('Select count(*) from comic').fetchone()
  conn.close()
  return {"Records": res[0]} 

@app.route("/art",methods=['POST'])
def char_post():
  query = request.json['query']
  characters = query.split()
  if not characters:
    return {"pages": []},404

  r = char_search(characters)
  return r

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
  characters = [c.lower() for c in characters]
  # Not sure if group by and having is the correct method
  question_marks = ','.join('?'*len(characters))
  sql_stmt = ('SELECT comic.page, comic.url, comic.title, comic.date,'
              ' count(*) n FROM chars'
              ' INNER JOIN comic ON'
              ' comic.page = chars.page'
              ' WHERE lower(CHARACTER) IN ({}) group by comic.page having n == {}'
              ' ORDER BY comic.page;')
  prep_sql_stmt=sql_stmt.format(question_marks,len(characters)) 
  conn = get_db_connection(app.config['DATABASE'])
  rows = conn.execute(prep_sql_stmt,characters).fetchall()
  conn.close()
  print("Getting all pages with {}".format(characters))

  response = []
  for r in rows:
    page_dic = {'number':r['page'],
                'url': r['url'],
                'title': r['title'],
                'date': r['date']}
    response.append(page_dic)

  return response 
