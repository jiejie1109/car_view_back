# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2025/1/3 9:15
# @File    : getCenterLeft.py
# @Software: PyCharm
import json
import time
from .getPublicData import *


def getPieBrandData():
    cars = list(getAllCars())
    carsVolume = {}
    for i in cars:
        if carsVolume.get(i.brand, -1) == -1:
            carsVolume[str(i.brand)] = int(i.saleVolume)
        else:
            carsVolume[str(i.brand)] += int(i.saleVolume)

    carsVolume = sorted(zip(carsVolume.values(), carsVolume.keys()), reverse=True)
    # print(carsVolume)
    return carsVolume
