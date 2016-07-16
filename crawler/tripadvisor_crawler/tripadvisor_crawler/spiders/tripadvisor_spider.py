import scrapy
from tutorial.items import PostItem
class TripAdvisorSpider(scrapy.Spider):
    name = "tripadvisor"
    allowed_domains = ["tripadvisor.com"]

    #crawl everything in under a page
    start_urls = [
        "https://www.tripadvisor.com/ShowForum-g298566-i2803-Osaka_Osaka_Prefecture_Kinki.html",
    ]
    def parse(self, response):
        for sel in response.xpath('//tr/td/b'):
            #print(sel.xpath('a/@href').extract()[0])
            url = 'https://www.tripadvisor.com/' + (sel.xpath('a/@href')[0].extract())
            yield scrapy.Request(url, callback=self.parse_articles_follow_next_page)

        next_page = response.xpath('//div[@class="pagination"]/div[@id="pager_top2"]/a[@class="guiArw sprite-pageNext"]/@href')

        if next_page:
            url = 'https://www.tripadvisor.com/' + next_page[0].extract()
            yield scrapy.Request(url, self.parse)

    def parse_articles_follow_next_page(self, response):
        for sel in response.xpath('//div[@class="postcontent"]'):
            item = PostItem()
            item['post_body'] = sel.xpath('div[@class="postBody"]/p/text()').extract()
            item['post_date'] = sel.xpath('div[@class="postDate"]/text()').extract()
            yield item

        next_page = response.xpath(
            '//div[@class="pagination"]/div[@id="pager_top2"]/a[@class="guiArw sprite-pageNext"]/@href')

        if next_page:
            url = 'https://www.tripadvisor.com/' + next_page[0].extract()
            yield scrapy.Request(url, self.parse_articles_follow_next_page)