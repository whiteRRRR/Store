from django.shortcuts import render

from .models import Order


def cart(request):

    name = 'Корзина'

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user.id, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order, 'name': name}
    return render(request, 'cart/cart.html', context=context)


def checkout(request):

    name = 'Заказ'

    if request.user.is_authenticated:
        user = request.user.user_id
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order, 'name': name}
    return render(request, 'cart/checkout.html', context=context)
