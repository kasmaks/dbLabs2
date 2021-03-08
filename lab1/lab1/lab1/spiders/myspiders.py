import scrapy
from scrapy.linkextractors import LinkExtractor
from lab1.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = "NewsSpider"
    allowed_domains = ["tsn.ua"]
    start_urls = ["https://tsn.ua/"]
    urls = ["https://tsn.ua/"]

    def parse_news_page(self, response):
        news_item = NewsItem()
        news_item['text'] = []
        news_item['image_url'] = []
        news_item['page_url'] = response.request.url
        for text in response.xpath("//*[not(self::script) and not(self::style)]/text()"):
            if len(text.extract().strip()) > 0:
                news_item['text'].append(text.extract().strip())

        for image_url in response.xpath("//img/@src | //img/@data-src"):
            news_item['image_url'].append(image_url.extract())

        yield news_item

    def parse(self, response, ):
        request = scrapy.Request(response.urljoin(self.start_urls[0]), callback=self.parse_news_page)
        yield request

        for link in LinkExtractor(allow_domains=self.allowed_domains).extract_links(response):
            self.urls.append(link.url)
            request = scrapy.Request(link.url, callback=self.parse_news_page)
            yield request
            if len(self.urls) == 20:
                break
