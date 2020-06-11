import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class MySpider(CrawlSpider):
    name = 'start'
    handle_httpstatus_list = [301, 302]

    def __init__(self, **kwargs):
        self.allowed_domains = [f"{kwargs.get('domain')}"]
        self.start_urls = [f"{kwargs.get('url')}"] 
        self.rules = (
            Rule(LinkExtractor(), callback='parse_item', follow=True),
            )
        super(MySpider, self).__init__(**kwargs)  

    def parse_item(self, response):
        if response.status == 301 or 302:
            print(f'{response.url} -> {response.status}')
        else:
            exit()
       
