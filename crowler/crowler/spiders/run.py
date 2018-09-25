# -*- coding: utf-8 -*-
#scrapy crawl run -o 20180710.json ←実行コマンド
import scrapy
from crowler.items import CrowlerItem


URL="http://qiita.com"
year="2018"
month="Sep"
day="20"
time=month+" "+day+", "+year

class RunSpider(scrapy.Spider):
    name = 'run'
    allowed_domains = ['qiita.com']
    start_urls = ['http://qiita.com/items/']

    def parse(self, response):
        flag=0
        for i in range(1,21):
            address = response.xpath(f'//*[@id="main"]/div/div/div[1]/article[{i}]/div/div[1]/text()').extract_first()
            if time in address:
                flag=1
                bodypage=response.xpath(f'//*[@id="main"]/div/div/div[1]/article[{i}]/div/div[2]/a/@href').extract()
                bodypageurl=[URL+bodypage[0]]
                for bodyurl in bodypageurl:
                    yield scrapy.Request(bodyurl, callback=self.parsebody)
            elif flag:
                return 0

        nextpass = response.xpath('//*[@id="main"]/div/div/div[1]/div/ul/li[2]/a/@href').extract()
        next_urls=[URL+nextpass[0]]
        for url in next_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parsebody(self,response):
        item=CrowlerItem()
        link=response.url
        link=link.split("/")
        item["title"]=response.xpath('/html/head/title/text()').extract()
        item["body"]=response.xpath(f'//*[@id="item-{link[5]}"]//text()').extract()
        item["code"]=response.xpath('//pre//text()').extract()
        yield item
