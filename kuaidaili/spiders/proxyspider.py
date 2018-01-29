# -*- coding: utf-8 -*-
import scrapy
from ..items import KuaidailiItem

class ProxyspiderSpider(scrapy.Spider):
    name = 'proxyspider'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']

    base_url = 'https://www.kuaidaili.com/free/inha/'
    offset = 1

    def parse(self, response):

        proxys = response.xpath("//div[@id='list']//tbody/tr")

        for proxy in proxys:
            item = KuaidailiItem()
            item['ip'] = proxy.xpath(".//td[1]/text()").extract_first()
            item['port'] = proxy.xpath(".//td[2]/text()").extract_first()
            item['type'] = proxy.xpath(".//td[4]/text()").extract_first()
            item['response_speed'] = proxy.xpath(".//td[6]/text()").extract_first()
            item['check_time'] = proxy.xpath(".//td[7]/text()").extract_first()

            yield item

        self.offset +=1
        next_url = self.base_url+str(self.offset)

        yield scrapy.Request(next_url,callback=self.parse)