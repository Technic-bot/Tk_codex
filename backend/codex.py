import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['DATABASE'] = app.root_path + "/db/" +app.config['DB_NAME']

def get_db_connection(db_file):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/test")
def test_api():
  """Test endpoint to verify connectivity"""
  conn = get_db_connection(app.config['DATABASE'])
  res = conn.execute('Select count(*) from comic').fetchone()
  conn.close()
  return {"Records": res[0]} 

@app.route("/dialogue",methods=['POST'])
def dialogue():
  """ Get matching dialogue 
      Matches some arbitrary text to some dialogue
      by one or more characters
  """
  chars = request.json['characters'].split()
  chars = [c.lower() for c in chars]
  text  = request.json['text']
  if not text or not chars:
    return {"pages": []},404

  question_marks = ','.join('?'*len(chars))
  sql_stmt = ('SELECT comic.page, comic.url, comic.title, comic.date'
              ' FROM comic'
              ' INNER JOIN script ON'
              ' comic.page == script.page'
              ' WHERE lower(script.speaker) IN ({})'
              ' AND  lower(script.dialogue) like ? '
              ' ORDER BY comic.page;')
  sql_stmt = sql_stmt.format(question_marks)
  
  proc_query = '%' + text.lower() + '%'
  sub_arr = chars + [proc_query]
  conn = get_db_connection(app.config['DATABASE'])
  rows = conn.execute(sql_stmt,sub_arr).fetchall()
  conn.close()

  response = []

  for r in rows:
    page_dic = {'number':r['page'],
                'url': r['url'],
                'title': r['title'],
                'date': r['date']}
    response.append(page_dic)

  return jsonify(response)

@app.route("/art",methods=['POST'])
def char_post():
  """ Check for art
      Searches for one or more character
      that had dialogue in one page
  """
  query = request.json['query']
  characters = query.split()
  if not characters:
    return {"pages": []},404

  r = char_search(characters)
  return r

@app.route("/text",methods=['POST'])
def text_post():
  query = request.json['query']
  if not query:
    return {"pages": []},404


  proc_query = '%' + query.lower() + '%'
  sql_stmt = ('SELECT page,url,title,date FROM comic '
              'WHERE lower(transcript) like ? ORDER BY page;')
  
  conn = get_db_connection(app.config['DATABASE'])
  rows = conn.execute(sql_stmt,(proc_query,)).fetchall()
  conn.close()

  response = []

  for r in rows:
    page_dic = {'number':r['page'],
                'url': r['url'],
                'title': r['title'],
                'date': r['date']}
    response.append(page_dic)
  return jsonify(response)


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
  """Query DB for characters in pages"""
  characters = [c.lower() for c in characters]
  # Not sure if group by and having is the correct method
  question_marks = ','.join('?'*len(characters))
  sql_stmt = ('SELECT comic.page, comic.url, comic.title, comic.date,'
              ' count(*) n FROM chars'
              ' INNER JOIN comic ON'
              ' comic.page == chars.page'
              ' WHERE lower(CHARACTER) IN ({}) group by comic.page having n == {}'
              ' ORDER BY comic.page;')
  prep_sql_stmt=sql_stmt.format(question_marks,len(characters)) 
  conn = get_db_connection(app.config['DATABASE'])
  rows = conn.execute(prep_sql_stmt,characters).fetchall()
  conn.close()
  #print("Getting all pages with {}".format(characters))

  response = []
  for r in rows:
    page_dic = {'number':r['page'],
                'url': r['url'],
                'title': r['title'],
                'date': r['date']}
    response.append(page_dic)

  return jsonify(response)
