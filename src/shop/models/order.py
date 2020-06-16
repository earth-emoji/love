import uuid
from django.db import models

from accounts.models import Member

class Order(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    ref_code = models.CharField(max_length=15)
    customer = models.ForeignKey(Member, related_name='orders', on_delete=models.SET_NULL, null=True)
    is_fulfilled = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} - {1}'.format(self.customer, self.ref_code)

    @property
    def get_order_total(self):
        return sum([item.product.price for item in self.items.all()])
