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

