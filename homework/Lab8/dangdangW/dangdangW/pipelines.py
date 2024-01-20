# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
    
class DangdangwPipeline(object):  
    def process_item(self, item, spider):  
        with open('dangdang.csv', 'a',newline="") as csvfile:  
            fieldnames = ['author', 'name', 'price']  
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
            if csvfile.tell()==0:
                writer.writeheader()  

            writer.writerow(item)  
        return item