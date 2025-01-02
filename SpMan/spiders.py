# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/12/30 10:44
# @File    : spiders.py.py
# @Software: PyCharm

import requests
from lxml import etree
import csv
import os
import time
import json
import pandas
import re
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_view.settings')
django.setup()
from myApp.models import CarInfo


class spider(object):
    def __init__(self):
        self.spider = 'https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&city_name=%E6%88%90%E9%83%BD&count=10&&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&series_type=&nation=0'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
        }

    def init(self):
        if not os.path.exists('./temp.csv'):
            with open('./temp.csv', 'a', encoding='utf-8', newline='') as wf:
                writer = csv.writer(wf)
                writer.writerow(["brand", "carName", "carImg", "saleVolume", "price", "manufacturer", "rank",
                                 "carModel", "energyType", "marketTime", "insure"])

    def get_page(self):
        with open('./spiderPage.txt', 'r', encoding='utf-8') as r_f:
            return r_f.readlines()[-1].strip()

    def set_page(self, newPage):
        with open('./spiderPage.txt', 'a', encoding='utf-8') as a_f:
            a_f.write('\n' + str(newPage))

    def main(self):
        count = self.get_page()
        params = {
            'offset': int(count)
        }
        print("数据从{}开始爬取".format(int(count) + 1))
        pageJson = requests.get(url=self.spider, headers=self.headers, params=params).json()
        pageJson = pageJson['data']['list']
        try:
            for index, car in enumerate(pageJson):
                # 存储汽车的数据
                carData = []
                print("正在爬取中%d" % (index + 1) + "数据")
                # 品牌名
                carData.append(car['brand_name'])
                # 车名
                carData.append(car["series_name"])
                # 图片链接
                carData.append(car["image"])
                # 销量
                carData.append(car["count"])
                # 价格
                price = [car["min_price"], car["max_price"]]
                carData.append(price)
                # 厂商
                carData.append(car["sub_brand_name"])
                # 排名
                carData.append(car["rank"])
                # 第二页
                carNumber = car["series_id"]
                infoHTML = requests.get("https://www.dongchedi.com/auto/params-carIds-x-%s" % carNumber,
                                        headers=self.headers)
                infoHTMLpath = etree.HTML(infoHTML.text)
                # 车型
                carModel = infoHTMLpath.xpath("//div[@data-row-anchor='jb']/div[2]/div/text()")[0]
                carData.append(carModel)
                # 能源类型
                energyType = infoHTMLpath.xpath("//div[@data-row-anchor='fuel_form']/div[2]/div/text()")[0]
                carData.append(energyType)
                # 上市时间
                marketTime = infoHTMLpath.xpath("//div[@data-row-anchor='market_time']/div[2]/div/text()")[0]
                carData.append(marketTime)
                # 保修期限
                insure = infoHTMLpath.xpath("//div[@data-row-anchor='period']/div[2]/div/text()")[0]
                carData.append(insure)
                print(carData)
                self.save_to_csv(carData)
        except:
            pass
            # break
        # print(pageJson)
        self.set_page(int(count) + 10)
        self.main()

    def save_to_csv(self, result_data):
        with open('./temp.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(result_data)

    def clear_csv(self):
        df = pandas.read_csv('./temp.csv')
        # 删除空行
        df.dropna(inplace=True)
        # 删除重复
        df.drop_duplicates(inplace=True)
        print("总数量为%d" % df.shape[0])
        return df.values

    def save_to_mysql(self):
        data = self.clear_csv()
        for car in data:
            CarInfo.objects.create(brand=car[0],
                                   carName=car[1],
                                   carImg=car[2],
                                   saleVolume=car[3],
                                   price=car[4],
                                   manufacturer=car[5],
                                   rank=car[6],
                                   carModel=car[7],
                                   energyType=car[8],
                                   marketTime=car[9],
                                   insure=car[10],
                                   )


if __name__ == '__main__':
    spiderObj = spider()
    # spiderObj.init()
    # spiderObj.main()
    spiderObj.save_to_mysql()