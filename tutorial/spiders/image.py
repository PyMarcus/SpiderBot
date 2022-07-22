import asyncio
import aiofiles as aiofiles
import requests
import scrapy


class ImageSpider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['example.com']
    start_urls = ['https://pt.wikipedia.org/wiki/Portal:Biografias']

    def parse(self, response):
        urls = list()
        image_urls = response.css("a.image img::attr(src)").getall()
        for image in image_urls:
            url = response.urljoin(image)
            urls.append(url)
            self.imageDownload(urls)

    def imageDownload(self, response):
        for links in response:
            response = requests.get(url=links, verify=False)
            asyncio.run(self.save(response))

    async def save(self, response):
        async with aiofiles.open(f"./images/{response.url.replace(':', '').replace('/', '')}.jpg", 'wb') as f:
            await f.write(response.content)
