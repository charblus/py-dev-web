import requests
from lxml import etree

url= 'https://book.douban.com/subject/1084336/comments'

r = requests.get(url).text
  
s = etree.HTML(r)
file = s.xpath('//*[@id="comments"]/ul/li/div[2]/p/span/text()')[0].strip()
file.encode('utf-8')
print(file)
