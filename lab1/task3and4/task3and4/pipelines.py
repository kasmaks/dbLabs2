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


def xml_to_xslt():
    xslt_root = etree.parse("../files/task4.xslt")

    transform = etree.XSLT(xslt_root)
    doc = etree.parse("../files/task3.xml")
    result = transform(doc)
    print(result)
    result.write("../files/task4.html", pretty_print=True, encoding="UTF-8")


class StorePipeline:

    def __init__(self):
        self.data = etree.Element("items")

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        write_to_xml(self.data, "../files/task3.xml")
        xml_to_xslt()

    def process_item(self, item, spider):
        i = etree.SubElement(self.data, "item")

        price = etree.SubElement(i, "price")
        price.text = item["price"]

        price = etree.SubElement(i, "description")
        price.text = item["description"]

        price = etree.SubElement(i, "image_url")
        price.text = item["image_url"]
        return item
