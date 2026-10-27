import scrapy

class BooksXPathSpider(scrapy.Spider):
    name = 'books_xpath'
    custom_settings = {
        'LOG_ENABLED': False
    }
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.xpath('//article[@class="product_pod"]'):
            title = book.xpath('.//h3/a/@title').get()
            price = book.xpath('.//p[@class="price_color"]/text()').get()
            availability = book.xpath('.//p[contains(@class, "availability")]/text()').getall()[-1].strip()
            yield {
                'title': title,
                'price': price.replace('£', ''),
                'availability': availability
            }
