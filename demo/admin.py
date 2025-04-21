from django.contrib import admin
from demo.models import (
    Customer,
    Product,
    Cart,
    OrederPlace
)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','name','locality','city','state']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','selling_price','discount_price','description','category','brand','image']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer','product','quantity']

@admin.register(OrederPlace)
class OrederPlaceAdmin(admin.ModelAdmin):
    list_display = ['customer','product','cart','quantity','ordered_date','status',]

