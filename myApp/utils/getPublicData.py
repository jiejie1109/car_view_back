
from myApp.models import *


# 返回所有车辆
def getAllCars():
    return CarInfo.objects.all()
