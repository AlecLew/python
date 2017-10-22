import urllib.request

url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=998407.O'
res = urllib.request.urlopen(url)
html = res.read().decode('utf-8')
print(html)
