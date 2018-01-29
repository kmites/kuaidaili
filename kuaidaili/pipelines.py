# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class KuaidailiPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='xxxxx', db='kuaidaili',charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into proxyinfo(p_port,p_type,p_speed,p_time,p_ip) values(%s,%s,%s,%s,%s)'
        try:
            self.cur.execute(sql,(item['port'],item['type'],item['response_speed'],item['check_time'],item['ip']))
            self.conn.commit()

        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()
