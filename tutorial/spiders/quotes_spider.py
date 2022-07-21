import asyncio
import scrapy
import aiofiles


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # @overrite
    def start_requests(self):
        """
        make requests (async) to urls defined
        :return:
        """
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  # make request async and call back parse to response

    def parse(self, response):
        """
        next page
        :param response:
        :return:
        """
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    async def readFile(self, page_name, response):
        """
        Write in files asyncronous (the page html) of request
        :param page_name:
        :param response:
        :return:
        """
        async with aiofiles.open(f"quotes-{page_name}.html", 'wb') as f:
            await f.write(response.body)

    def getLinks(self, response):
        """
        Get links
        :param response:
        :return:
        """
        links = response.css('a.tag::attr(href)').getall()
        print(links)

    def getTitle(self, response):
        """
        Get title
        :param response:
        :return:
        """
        title = response.xpath('.//h1/a/text()').get()
        print(f"title: {title}")

    def getNextPage(self, response):
        """
        go to the next page
        :param response:
        :return:
        """
        next_page = response.css('li.next a::attr(href)').get()
        print(f"[*] Access another page {response.urljoin(next_page)}")
        next_page = response.css('li.next a::attr(href)').get()
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

    """
        # @override
    def parse(self, response, **kwargs):
        page = response.url.split('/')[-2]
        asyncio.run(self.readFile(page, response))
        self.log(f"SAVED FILE: {page}")
        # links
        self.getLinks(response)
        self.getTitle(response)
        self.new_parse(response)
        # [scrapy.Request(url=x.url, callback=self.parse) for x in self.getNextPage(response)]

    """