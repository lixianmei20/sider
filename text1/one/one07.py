# import urllib.request
#
# response = urllib.request.urlopen('https://httpbin.org/get')
# print(response.read().decode())
import urllib.request

# 假设你从某个网站获取了一个免费代理列表，这里我们手动指定一个
proxy_ip = 'http://127.0.0.1:7980'  # 示例代理IP和端口

# 创建代理处理器
proxy_handler = urllib.request.ProxyHandler({'http': proxy_ip, 'https': proxy_ip})

# 创建opener
opener = urllib.request.build_opener(proxy_handler)

# 安装opener
urllib.request.install_opener(opener)

# 现在你可以使用urllib.request进行请求了，请求会通过代理发送
response = urllib.request.urlopen('http://httpbin.org/ip')
print(response.read().decode('utf-8'))  # 查看响应，通常httpbin.org/ip会返回你的IP地址