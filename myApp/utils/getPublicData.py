# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/12/31 9:13
# @File    : getPublicData.py
# @Software: PyCharm

from myApp.models import *


# 返回所有车辆
def getAllCars():
    return CarInfo.objects.all()
