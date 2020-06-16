from django import template
from shop.models import Basket

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        return user.customer.basket.items.count()
    return 0
