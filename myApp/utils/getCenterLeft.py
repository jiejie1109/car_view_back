import json
import time
from .getPublicData import *

# 饼图
def getPieBrandData():
    cars = list(getAllCars())
    carsVolume = {}
    for i in cars:
        if carsVolume.get(i.brand, -1) == -1:
            carsVolume[str(i.brand)] = int(i.saleVolume)
        else:
            carsVolume[str(i.brand)] += int(i.saleVolume)

    carsVolume = sorted(zip(carsVolume.values(), carsVolume.keys()), reverse=True)
    sortDict = [{'name': v, 'value': k} for k, v in carsVolume][:10]
    # print(sortDict)
    return sortDict
