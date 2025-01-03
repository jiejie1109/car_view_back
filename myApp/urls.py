# -*- coding: utf-8 -*-
# @Author  : DaiYuJie
# @Time    : 2024/12/31 9:09
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from myApp import views

urlpatterns = [
    path("center/", views.center, name="center"),
    path("centerLeft/", views.centerLeft, name="centerLeft")
]
