from django.contrib import admin

from shop.models import Basket, Order, OrderItem

admin.site.register(Basket)
admin.site.register(Order)
admin.site.register(OrderItem)
