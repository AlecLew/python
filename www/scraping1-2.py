import urllib.request
import re

url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=998407.O'
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
response.close()


r = re.compile('<td class="stoksPrice">(\d+[,.])*\d+</td>')
m = r.search(html)
s = m.group(0)
print(s)

