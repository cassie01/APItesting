import requests as r

html = r.get('https://cn.bing.com')
content = html.text
with open(r'bing.txt', 'w', encoding= 'utf-8') as f:
    f.write(str(content))