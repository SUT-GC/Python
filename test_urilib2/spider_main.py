# coding:utf-8
#_*_ coding:utf-8 _*_

import url_manage, html_output, html_download, html_parser
class SpiderMain:
	def __init__(self):
		self.urls = url_manage.UrlManager()
		self.downloader = html_download.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.output = html_output.HtmlOutputer()

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			new_url = self.urls.get_new_url()
			print "第%d 个url ：%s " % (count,new_url)
			html_cont = self.downloader.downloade(new_url)
			new_urls, new_data = self.parser.parse(new_url,html_cont)
			self.urls.add_new_urls(new_urls)
			self.output.collect_data(new_data)
			if count == 1000:
				break
			count = count + 1
			print "craw success"

		self.output.output_html()

if __name__ == '__main__':
	root_url ='http://baike.baidu.com/view/21087.htm'
	obj_spider = SpiderMain()
	obj_spider.craw(root_url) 