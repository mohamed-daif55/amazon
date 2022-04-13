import scrapy


class WatchesDataSpider(scrapy.Spider):
    name = 'watches_data'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/s?k=watches+for+men&sprefix=%2Caps%2C180&ref=nb_sb_ss_recent_1_0_recent']

    def parse(self, response):
        for product in response.xpath("//div[@class='a-section a-spacing-base']"):
            yield {
                'title' : product.xpath(".//div[@class='a-section a-spacing-small s-padding-left-small s-padding-right-small']/div[1]/h2/a/span/text()").get(),
                'price' : product.xpath(".//div[@class='a-row a-size-base a-color-base']/a/span/span[1]/text()").get(),
                'rating' : product.xpath(".//div[@class='a-section a-spacing-none a-spacing-top-micro']/div[1]/span/span/a/i/span/text()").get(),
                'image' : product.xpath(".//div[@class='a-section aok-relative s-image-square-aspect']/img[1]/@src").get()
            }
