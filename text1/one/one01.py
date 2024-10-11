import urllib.request

import requests
from bs4 import BeautifulSoup

# 创建一个申请（request如同一个URL）
h = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
req = urllib.request.Request("https://movie.douban.com/top250", headers=h)

r = urllib.request.urlopen(req)

# print(r.status)
# print(r.read().decode())
html_doc=r.read().decode()
soup=BeautifulSoup(html_doc,'html.parser')
items=soup.find_all("div",class_="item")
for item in items:
    img=item.find("div",class_="pic").a.img
    print(img)
    print("="*50)
# for item in items:
#     img = item.find("div", class_="pic").a.img
#     print(img)
#     print("=" * 50)


