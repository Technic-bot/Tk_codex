# Estos comentarios en español estan dedicados a TeapotOfDoom
# Prueba generica para verificar que el API se levanta
def test_test(client):
  resp = client.get('/test')
  print(resp.json)
  assert isinstance(resp.json['Records'],int)

# Prueba que podamos hacer una consulta multi personajes
def test_art(client):
  payload = {"query":"Dahlia Keiren Daniels Therie"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/art',json=payload,headers=headers)
  page = resp.json[0]['number']
  assert page == 1181

# Prueba que los alias sirven 
def test_alias(client):
  payload = {"query":"Dahlia Kei Daniels Therie"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/art',json=payload,headers=headers)
  page = resp.json[0]['number']
  assert page == 1181

def test_alias_single(client):
  payload = {"query":"Nat"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/art',json=payload,headers=headers)
  page = resp.json[0]['number']
  assert page == 208

# Prueba que se funcionen la consultas textuales
def test_text(client):
  payload = {"query":"gay rumors"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/text',json=payload,headers=headers)
  page = resp.json[0]['number']
  assert page == 504

# Prueba para consultas de dialogos
# Estas consultan texto pero solo sobre uno o mas personajes
def test_dialogue_single(client):
  payload = {"characters":"Natani","text":"gay rumors"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/dialogue',json=payload,headers=headers)
  page = resp.json[0]['number']
  assert page == 504

# Usando aliases
def test_dialogue_alias_single(client):
  payload = {"characters":"Nat","text":"gay rumors"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/dialogue',json=payload,headers=headers)
  page = resp.json[0]['number']
  assert page == 504

# Misma prueba pero para multiples personajes
def test_dialogue_multi(client):
  payload = {"characters":"Natani keith","text":"gay"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/dialogue',json=payload,headers=headers)
  pages = []
  for page in resp.json:
    pages.append(int(page['number']))

  exp_pages = [236,282,504]
  matches =   [e in pages for e in exp_pages]
  assert all(matches) 

# Misma prueba pero para aliases
def test_dialogue_aliases(client):
  payload = {"characters":"Nat keith","text":"gay"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/dialogue',json=payload,headers=headers)
  pages = []
  for page in resp.json:
    pages.append(int(page['number']))

  exp_pages = [236,282,504]
  matches =   [e in pages for e in exp_pages]
  assert all(matches) 

