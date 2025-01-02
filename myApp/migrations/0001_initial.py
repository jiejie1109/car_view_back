# Generated by Django 5.1.4 on 2024-12-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarInfo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="id"
                    ),
                ),
                (
                    "brand",
                    models.CharField(default="", max_length=255, verbose_name="品牌"),
                ),
                (
                    "carName",
                    models.CharField(default="", max_length=255, verbose_name="车名"),
                ),
                (
                    "carImg",
                    models.CharField(default="", max_length=255, verbose_name="图片链接"),
                ),
                (
                    "saleVolume",
                    models.CharField(default="", max_length=255, verbose_name="销量"),
                ),
                (
                    "price",
                    models.CharField(default="", max_length=255, verbose_name="价格"),
                ),
                (
                    "manufacturer",
                    models.CharField(default="", max_length=255, verbose_name="厂商"),
                ),
                (
                    "rank",
                    models.CharField(default="", max_length=255, verbose_name="排名"),
                ),
                (
                    "carModel",
                    models.CharField(default="", max_length=255, verbose_name="车型"),
                ),
                (
                    "energyType",
                    models.CharField(default="", max_length=255, verbose_name="能源类型"),
                ),
                (
                    "marketTime",
                    models.CharField(default="", max_length=255, verbose_name="上市时间"),
                ),
                (
                    "insure",
                    models.CharField(default="", max_length=255, verbose_name="保修时间"),
                ),
                (
                    "creatTime",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
            options={
                "db_table": "carInfo",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="id"
                    ),
                ),
                (
                    "username",
                    models.CharField(default="", max_length=255, verbose_name="用户名"),
                ),
                (
                    "password",
                    models.CharField(default="", max_length=255, verbose_name="密码"),
                ),
                (
                    "creatTime",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
