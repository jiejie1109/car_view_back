
import json
import time
from .getPublicData import *


def getBaseData():
    cars = getAllCars()
    # 总车数
    sumCar = len(cars)
    # 销量最多的汽车
    highVolume = cars[0].saleVolume
    topCar = cars[0].carName

    # 车型
    carModels = {}
    MaxModel = 0
    mostModel = ""
    # 判断销量最多的车型
    for i in cars:
        if carModels.get(i.carModel, -1) == -1:
            carModels[i.carModel] = 1
        else:
            carModels[i.carModel] += 1
    #  对结果进行排序 carModels.items()会返回一个视图对象，它展示了字典 carModels 的所有键值对
    #   key=lambda x: x[1] carModels.items()的视图对象，x[1]表示按照字典的值进行排序，reverse=True表示降序排序
    carModels = sorted(carModels.items(), key=lambda x: x[1], reverse=True)
    mostModel = carModels[0][0]

    # 品牌
    carBrand = {}
    maxBrand = 0
    mostBrand = ''
    for i in cars:
        if carBrand.get(i.brand, -1) == -1:
            carBrand[i.brand] = 1
        else:
            carBrand[i.brand] += 1
    for k, v in carBrand.items():
        if v > maxBrand:
            maxBrand = v
            mostBrand = k
    # 车辆平均价
    carPrice = {}
    avgPrice = 0
    sumPrice = 0
    for i in cars:
        x = json.loads(i.price)[0] + json.loads(i.price)[1]
        sumPrice += x
    avgPrice = sumPrice / (sumCar * 2)
    avgPrice = round(avgPrice, 2)
    return sumCar, highVolume, topCar, mostModel, mostBrand, avgPrice


def getRollData():
    cars = list(getAllCars())
    # 品牌
    carBand = {}
    for i in cars:
        if carBand.get(i.brand, -1) == -1:
            carBand[str(i.brand)] = 1
        else:
            carBand[str(i.brand)] += 1
    brandList = [(v, k) for k, v in carBand.items()]
    brandList = sorted(brandList, reverse=True)[:10]
    # 变成字典
    sorDict = {i[1]: i[0] for i in brandList}
    # 变成name value形式的列表
    resultList = [{'name': k, 'value': v} for k, v in sorDict.items()]
    # print(resultList)
    return resultList


def getTypeRate():
    cars = list(getAllCars())
    # 能量类型
    carType = {}
    for i in cars:
        if carType.get(i.energyType, -1) == -1:
            carType[str(i.energyType)] = 1
        else:
            carType[str(i.energyType)] += 1
    oilRate = round(carType['汽油'] / len(cars) * 100, 2)
    electricRate = round(carType['纯电动'] / len(cars) * 100, 2)
    mixRate = round(carType['插电式混合动力'] / len(cars) * 100, 2)
    # print(carType, oilRate, electricRate, mixRate)
    return oilRate, electricRate, mixRate
