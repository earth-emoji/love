import uuid
from django.db import models

from accounts.models import Member
from catalog.models import Product
from shop.models import Basket, Order

class OrderItem(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.SET_NULL, null=True, blank=True)
    basket = models.ForeignKey(Basket, on_delete=models.SET_NULL, related_name='items', null=True, blank=True)
    vendor = models.ForeignKey(Member, related_name='order_items', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, null=True, blank=True)
    is_fulfilled = models.BooleanField(default=False)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    @property
    def get_customer(self):
        return self.order.customer.get_name

    def __str__(self):
        return self.product.name