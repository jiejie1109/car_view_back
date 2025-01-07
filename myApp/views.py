from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .utils import getCenterData
from .utils import getPublicData
from .utils import getCenterLeft
from .utils import getBottomLeftData
from .utils import getCenterRightData


# Create your views here.

def center(request):
    if request.method == "GET":
        sumCar, highVolume, topCar, mostModel, mostBrand, avgPrice = getCenterData.getBaseData()
        SortList = getCenterData.getRollData()
        oilRate, electricRate, mixRate = getCenterData.getTypeRate()
        return JsonResponse({
            "sumCar": sumCar,
            "highVolume": highVolume,
            "topCar": topCar,
            "mostModel": mostModel,
            "mostBrand": mostBrand,
            "avgPrice": avgPrice,
            "SortList": SortList,
            "oilRate": oilRate,
            "electricRate": electricRate,
            "mixRate": mixRate,
        })


def centerLeft(request):
    if request.method == "GET":
        sortDict = getCenterLeft.getPieBrandData()
        return JsonResponse({
            "sortDict": sortDict,
        })


def bottomLeft(request):
    if request.method == "GET":
        brandList, volumeList, priceList = getBottomLeftData.getSquareData()
        return JsonResponse({
            "brandList": brandList,
            "volumeList": volumeList,
            "priceList": priceList,
        })


def centerRight(request):
    if request.method == "GET":
        realDate = getCenterRightData.getPriceSortData()
        return JsonResponse({
            "realDate": realDate
        })
