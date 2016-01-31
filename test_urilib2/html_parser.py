#coding:utf-8
from bs4 import BeautifulSoup
import re, urlparse
class HtmlParser(object):
	def parse(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return 

		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls, new_data

	def _get_new_urls(self, page_url, soup):
		urls = set()
		links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url,new_url)
			urls.add(new_full_url)
		return urls

	def _get_new_data(self,page_url,soup):
		data = {}
		title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
		data['title'] = title_node.text()
		summary_node = soup.find("div", class_="lemma-summary")
		data['summary']=summary_node.text()

		return data
