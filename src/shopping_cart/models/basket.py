import uuid
from django.db import models

from accounts.models import Member

class Basket(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    customer = models.OneToOneField(Member, on_delete=models.CASCADE, blank=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def empty_basket(self):
        self.items.clear()

    def __str__(self):
        return f"{self.customer.get_name}'s basket"