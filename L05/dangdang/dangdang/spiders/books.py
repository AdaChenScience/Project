import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.54.00.00.00.00.html"]

    def parse(self, response):
        book_list = response.css('.bigimg li')
        
        for book in book_list:
            title = book.css('.name a::attr(title)').get()
            author = book.css('.search_book_author > span:nth-child(1) > a::attr(title)').get()
            publisher = book.css('.search_book_author > span:nth-child(3) > a::text').get()
            price = book.css('.price span::text').get()
            yield {
                'title': title,
                'author': author,
                'publisher': publisher,
                'price': price
            }

        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
