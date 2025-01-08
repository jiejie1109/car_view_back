import json
import time
from .getPublicData import *
import re


def getRankData():
    cars = list(getAllCars())
    carData = []
    for car in cars[:20]:
        car.price = re.findall(r"[-+]?\d*\.\d+|\d+", car.price)
        # print(car.price)
        car.price = '-'.join(car.price)
        carData.append({
            'carName': car.carName,
            'brand': car.brand,
            'rank': car.rank,
            'carImg': car.carImg,
            'manufacturer': car.manufacturer,
            'carModel': car.carModel,
            'price': car.price,
            'saleVolume': car.saleVolume,
            'marketTime': car.marketTime,
            'insure': car.insure,
        })
    return carData
