# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
import sqlite3

class SqlLite3Pipeline(object):

    def open_spider(self, spider):
        self.connection = sqlite3.connect("watches.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE watches(
                    title TEXT,
                    price TEXT,
                    rating TEXT,
                    image TEXT
                )
            
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        self.connection.close()


    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO watches (title,price,rating,image) VALUES(?,?,?,?)

        ''', (
            item.get('title'),
            item.get('price'),
            item.get('rating'),
            item.get('image')
        ))
        self.connection.commit()
        return item
