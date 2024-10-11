import sysconfig
import ddddocr
import requests
from bs4 import BeautifulSoup

import requests
s=requests.session()
h = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate",
    "accept-language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}



proxies={
    "http": "127.0.0.1:7890"
}
login=s.get('https://www.nowapi.com/?app=account.login',headers=h,proxies=proxies)
print(login.text)
print(s.cookies.keys())
for item in s.cookies.iteritems():
    print(item[0],":",item[1])
soup=BeautifulSoup(login.text,'heml.parser')
image_url=soup.find_all(id='authCodeImg')[0]['src']
ocr=ddddocr.DdddOCR()
image=open("example")

data={
    'username':'lxm',
    'age':'21'

}

# r= requests.get('http://httpbin.org/get',headers=h,proxies=proxies,data=data)
# print(r.text)
