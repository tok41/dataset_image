from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from image_test.items import ImageTestItem

#from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request

class FooSpider(CrawlSpider):
    name = "image_test"
    allowed_domains = ["safebooru.donmai.us"]
    start_urls = ["http://safebooru.donmai.us"]

    rules = [Rule(LinkExtractor(), callback='parse_pageinfo', follow=True)]

    def parse_pageinfo(self, response):
        sel = Selector(response)
        item = ImageTestItem()
        hxs = HtmlXPathSelector(response)
        image_urls = hxs.select('//img/@src').extract()
        item['image_urls'] = ['http://safebooru.donmai.us/'+x for x in image_urls]
        #item = PageInfoItem()
        #item['URL'] = response.url
        #item['title'] = sel.xpath('/html/head/title/text()').extract()
        return item

#    def parse(self, response):
#        hxs = HtmlXPathSelector(response)
#
#        item = ImageTestItem()
#        image_urls = hxs.select('//img/@src').extract()
#        item['image_urls'] = ['http://safebooru.donmai.us/'+x for x in image_urls]
#        return item
