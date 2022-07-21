SCRAPY A FRAMEWORK TO BUILD WEBSCRAPING AND WEBCRAWLER

https://docs.scrapy.org/en/latest/intro/overview.html

Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival.
Even though Scrapy was originally designed for web scraping, it can also be used to extract data using APIs (such as Amazon Associates Web Services) or as a general purpose web crawler.

### start a project

    scrapy startproject tutorial

### run the project (first time)

    python -m venv venv

    .\venv\Scripts\activate

    pip install -r requirements

    scrapy crawl quotes


### run if u already install the requirements:

    scrapy crawl quotes


### save data how a json file

    scrapy crawl quotes -O quotes.json



