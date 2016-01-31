# _*_ coding:utf-8 _*_

from bs4 import BeautifulSoup
import urllib2

url = "http://www.baidu.com"

print "开始抓取Html"

response = urllib2.urlopen(url)
# data = response.read()
#print data

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding = 'utf-8')
nodes = soup.find_all("a")
for node in nodes:
	print node.text

print "你好"
