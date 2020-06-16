from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Member
from catalog.models import Product

from .extras import generate_order_id
from shop.models import Order, OrderItem, Basket

def get_user_pending_order(request):
    # get order for the correct user
    customer = get_object_or_404(Member, user=request.user)
    order = Order.objects.filter(customer=customer, is_fulfilled=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

@login_required()
def get_vendor_pending_orders(request, slug):
    template_name = 'orders/vendor_pending_orders.html'
    vendor = get_object_or_404(Member, user=request.user, slug=slug)
    orders = OrderItem.objects.filter(vendor=vendor, is_ordered=True, is_fulfilled=False)
    data = {}
    data['orders'] = orders
    return render(request, template_name, data)

@login_required()
def get_pending_orders(request):
    template_name = 'orders/pending_orders.html'
    orders = OrderItem.objects.filter(is_fulfilled=False)
    data = {}
    data['orders'] = orders
    return render(request, template_name, data)

@login_required()
def get_customer_pending_orders(request, slug):
    template_name = 'orders/customer_pending_orders.html'
    customer = Member.objects.get(slug=slug)
    orders = Order.objects.filter(customer=customer, is_fulfilled=False)
    data = {}
    data['orders'] = orders
    return render(request, template_name, data)

@login_required()
def get_order_details(request, slug):
    template_name = 'orders/order_details.html'
    context = {}
    order = Order.objects.get(slug=slug)
    context["order"] = order
    return render(request, template_name, context)

@login_required()
def get_customer_order_details(request, slug):
    template_name = 'orders/customer_order_details.html'
    order = Order.objects.get(slug=slug)
    data = {}
    data['order'] = order
    return render(request, template_name, data)

@login_required()
def get_vendor_order_details(request, slug):
    template_name = 'orders/vendor_order_details.html'
    order = OrderItem.objects.get(slug=slug, vendor=request.user.vendor)
    data = {}
    data['order'] = order
    return render(request, template_name, data)

@login_required()
def get_driver_order_details(request, slug):
    template_name = 'orders/driver_order_details.html'
    order = OrderItem.objects.get(slug=slug, driver=request.user.driver)
    data = {}
    data['order'] = order
    return render(request, template_name, data)

@login_required
def add_to_cart(request, slug):
    product = Product.objects.get(slug=slug)
    customer = get_object_or_404(Member, user=request.user)

    customer.basket.add_to_basket(product)

    messages.info(request, "item added to cart")
    return redirect('products:product-list')

@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect('shop:order_summary')


@login_required()
def order_details(request, template_name='shopping_cart/order_summary.html', **kwargs):
    customer = get_object_or_404(Member, user=request.user)
    context = {
        'order': customer.basket
    }
    return render(request, template_name, context)

def purchase_success(request):
    # a view signifying the transcation was successful
    customer = Member.objects.get(user=request.user)
    order = Order.objects.create(customer=customer, ref_code=generate_order_id())

    for item in customer.basket.get_cart_items():
        item.order = order
        item.is_ordered = True
        item.save()

        product = item.product
        product.sold = product.sold + 1
        product.stock_quantity = product.stock_quantity - 1
        product.save()

    customer.basket.empty_basket()
    
    return render(request, 'shopping_cart/purchase_success.html', {})