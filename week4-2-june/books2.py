import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            price = book.css('p.price_color::text').get().replace('£', '')
            availability = ''.join(book.css('p.instock.availability::text').getall()).strip()
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': float(price),
                'availability': availability
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)