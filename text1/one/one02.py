import urllib.request
import pymysql
from lxml import etree

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='douban250',
                             cursorclass=pymysql.cursors.DictCursor)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}


def get_first_text(list_of_texts):
    if list_of_texts:
        return list_of_texts[0].strip() if list_of_texts[0] is not None else ""
    return ""


urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i * 25)) for i in range(10)]

with connection:
    for url in urls:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        html_doc = response.read().decode('utf-8')
        html = etree.HTML(html_doc)

        lis = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for index, li in enumerate(lis, start=1):
            img = get_first_text(li.xpath('div/div[1]/a/img/@src'))
            title = get_first_text(li.xpath('div/div[2]/div[1]/a/span[1]/text()'))
            src = get_first_text(li.xpath('div/div[2]/div[1]/a/@href'))
            dictor = get_first_text(li.xpath('div/div[2]/div[2]/p[1]/text()'))
            # 注意：这里可能需要调整XPath来获取类型
            type = get_first_text(li.xpath('div/div[2]/div[2]/p[1]/span[2]/text()'))  # 假设类型在<span>标签内
            comment = get_first_text(li.xpath('div/div[2]/div[2]/div/span[4]/text()'))
            quote = get_first_text(li.xpath('div/div[2]/div[2]/p[2]/span/text()'))

            with connection.cursor() as cursor:
                sql = "INSERT INTO douban250movie (img, title, src, dictor, type, comment, quote) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (img, title, src, dictor, type, comment, quote))

            # 注意：由于使用了with connection:，这里不需要再显式调用connection.commit()，
# 因为with块结束时会自动提交事务。