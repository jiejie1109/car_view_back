from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .utils import getCenterData
from .utils import getPublicData


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
