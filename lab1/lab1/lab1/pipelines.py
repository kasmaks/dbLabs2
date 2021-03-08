# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from lxml import etree


def write_to_xml(data, filename):
    et = etree.ElementTree(data)
    et.write(filename, pretty_print=True, encoding="UTF-8")


class NewsPipeline:

    def __init__(self):
        self.data = etree.Element("data")
        self.min_number_of_images = 0
        self.page_url_with_min_number_of_images = ""

    def count_number_of_images(self, item):
        if self.min_number_of_images == 0 or len(item["image_url"]) < self.min_number_of_images:
            self.min_number_of_images = len(item["image_url"])
            self.page_url_with_min_number_of_images = item["page_url"]

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        write_to_xml(self.data, "../files/task1.xml")
        print("Page :", self.page_url_with_min_number_of_images)
        print("The minimum number of images :", self.min_number_of_images)

    def process_item(self, item, spider):
        self.count_number_of_images(item)

        page = etree.SubElement(self.data, "page")
        page.set("url", item["page_url"])

        for text in item["text"]:
            f = etree.SubElement(page, "fragment")
            f.set("type", "text")
            f.text = text

        for image_url in item["image_url"]:
            f = etree.SubElement(page, "fragment")
            f.set("type", "image")
            f.text = image_url

        return item

