import scrapy
from task3and4.items import StoreItem


class StoreSpider(scrapy.Spider):
    name = "NewsSpider"
    allowed_domains = ["wallet.ua"]
    start_urls = ["https://wallet.ua/c/f-backpacks-pol_muzhskoj/"]

    def parse(self, response, ):

        counter = 0
        for div in response.xpath("//div[@class='prd-wrap']"):
            item = StoreItem()
            item["price"] = div.xpath(".//span[@class='crate']/@data-rate").get()
            item["description"] = div.xpath(".//img[@class='first-picture lazy']/@title").get()
            item["image_url"] = "https://wallet.ua/" + div.xpath(".//img[@class='first-picture lazy']/@data-src").get()
            yield item
            counter += 1
            if counter == 20:
                break
