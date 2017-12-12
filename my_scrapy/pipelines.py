import uuid

import pymysql

from my_scrapy import settings


class MySQLStoreCnblogsPipeline(object):
    def __init__(self):
        print('初始化22222222222')
        self.con = pymysql.connect(host=self.host,
                                   user=settings.MYSQL_USER,
                                   passwd=settings.MYSQL_PASSWD,
                                   db=settings.MYSQL_DBNAME,
                                   charset=settings.MYSQL_CHARSET,
                                   port=settings.MYSQL_PORT)
        self.cursor = self.con.cursor()

    def process_item(self, item, spider):

        sql = 'insert into jian_shu(id,name,description,href) values (%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql, (int(uuid.uuid1()), item['name'], item['description'], item['href']))
            print("insert success")  # 测试语句
        except Exception as e:
            print('Insert error:', e)
            self.con.rollback()
        return item

    def close_spider(self, spider):
        print('关闭0000000000000')
        self.con.commit()
        self.con.close()
