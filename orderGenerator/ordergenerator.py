from urllib import request, parse

url = 'http://127.0.0.1:8080/transaction'
data = {'test1': 10, 'test2': 20}
data = parse.urlencode(data).encode()

req = request.Request(url, data=data)
response = request.urlopen(req)