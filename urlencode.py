from urllib import request
from urllib import parse
params = {'name':'张三','age':18,'greet':'hellow world'}
result = parse.urlencode(params)
# print(result)

# url = 'https://www.baidu.com/s?wd=刘德华'
url  = 'http://www.baidu.com/s'
param = {'wd':'张学友'}
qs  = parse.urlencode(param)
url = url + '?' + qs
resp = request.urlopen(url)
# print(resp.read())
print(parse.parse_qs(result))
