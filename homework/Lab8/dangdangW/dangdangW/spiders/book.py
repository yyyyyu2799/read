import scrapy
import bs4
# from ..items import DangdangItem
# 需要引用DangdangItem，它在items里面。因为是items在book.py的上一级目录，..items这是一个固定用法。

class DangdangwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    pass

class DangdangSpider(scrapy.Spider): #定义一个爬虫类DoubanSpider。
    name = 'dangdang'
    allowed_domains = ['http://bang.dangdang.com']
    start_urls = []
    for x in range(1, 4):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2019-0-1-1' + str(x)
        start_urls.append(url)

    def parse(self, response): #parse是默认处理response的方法。
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        elements = soup.find('ul', class_="bang_list clearfix bang_list_mode").find_all('li')
        for element in elements:
            item = DangdangwItem()
            item['name'] = element.find('div',class_="name").find('a')['title']
            '''item['author'] = element.find('div', class_="publisher_info").text
            item['price'] = element.find('div', class_="price").find('span', class_="price_n").text

            item['name'] = item['name'].replace('\xa5','')
            item['author']=item['author'].replace('\xa5','')
            item['price']=item['price'].replace('\xa5','')
            '''
            #print(item)
            yield item#   #yield item是把获得的item传递给引擎。
            
            
