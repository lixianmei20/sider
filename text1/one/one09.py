import urllib.request

h = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate",
    "accept-language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
req= urllib.request.Request("http://httpbin.org/get",headers=h)


# proxies  = {"http":"127.0.0.1:7890"}

proxies = {"http":"47.116.126.57:3128"}  #免费代理

proxy_handler = urllib.request.ProxyHandler(proxies = proxies)

opener = urllib.request.build_opener(proxy_handler)

r = opener.open(req)

print(r.read().decode())
