import uuid

import pymysql

from my_scrapy import settings


class MySQLStoreCnblogsPipeline(object):

    def process_item(self, item, spider):
        # 数据库连接
        con = pymysql.connect(host=settings.MYSQL_HOST,
                              user=settings.MYSQL_USER,
                              passwd=settings.MYSQL_PASSWD,
                              db=settings.MYSQL_DBNAME,
                              charset=settings.MYSQL_CHARSET,
                              port=settings.MYSQL_PORT)
        # 数据库游标
        cursor = con.cursor()

        sql = 'insert into jian_shu(id,name,description,href) values (%s,%s,%s,%s)'
        try:
            cursor.execute(sql, (int(uuid.uuid1()), item['name'], item['description'], item['href']))
            print("insert success")  # 测试语句
        except Exception as e:
            print('Insert error:', e)
            con.rollback()
        finally:
            print('成功插入', cursor.rowcount, '条数据')
            con.commit()
        con.close()
        return item
