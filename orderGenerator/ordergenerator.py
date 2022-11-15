import random
import urllib.parse

url = 'http://127.0.0.1:8080/transaction'
params = {'var1': 'some data', 'var2': 1337}
print(url + urllib.parse.urlencode(params))
