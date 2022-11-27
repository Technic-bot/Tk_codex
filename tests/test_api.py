def test_test(client):
  resp = client.get('/test')
  print(resp.json)
  assert isinstance(resp.json['Records'],int)

def test_art(client):
  payload = {"query":"Dahlia Keiren Daniels Therie"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/art',json=payload,headers=headers)
  page = resp.json[0]['number']
  assert page == 1181

def test_text(client):
  payload = {"query":"gay rumors"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/text',json=payload,headers=headers)
  page = resp.json[0]['number']
  assert page == 504

def test_dialogue_single(client):
  payload = {"characters":"Natani","text":"gay rumors"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/dialogue',json=payload,headers=headers)
  page = resp.json[0]['number']
  assert page == 504

def test_dialogue_multi(client):
  payload = {"characters":"Natani keith","text":"gay"}
  headers = {"Content-Type": "application/json"}
  resp = client.post('/dialogue',json=payload,headers=headers)
  pages = []
  for page in resp.json:
    pages.append(int(page['number']))

  print(pages)
  exp_pages = [236,282,504]
  matches =   [e in pages for e in exp_pages]
  assert all(matches) 

