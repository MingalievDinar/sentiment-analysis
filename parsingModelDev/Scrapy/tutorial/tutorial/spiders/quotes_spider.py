import scrapy


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    start_urls = ['http://irecommend.ru/category/mobilnye-telefony']
    def parse(self, response):
        # follow links to mobiles pages
        for href in response.css('div.citate a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_mobile)

        # follow pagination links
        next_page = response.css('li.pager-next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_mobile(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'rating': extract_with_css('span.rating::text'),
            'text': " ".join(response.css('div.description')[2].css('p::text').extract())
        }

