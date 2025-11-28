from django.db import models
from django.contrib import admin

class Product(models.Model):
    product_name=models.CharField(max_length=30,help_text="Enter product name")
    product_id=models.IntegerField(help_text="Enter product id")
    product_descr=models.CharField(max_length=50,help_text="Write description")
    product_price=models.IntegerField(help_text="Enter price")

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','product_id','product_descr','product_price']

# Create your models here.
