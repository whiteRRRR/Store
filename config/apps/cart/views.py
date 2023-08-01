from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from .models import CartItem, Products


class AddToCartView(View):

    def post(self, request, product_slug):
        if request.user.is_authenticated:
            product = get_object_or_404(Products, slug=product_slug)
            cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
            return redirect('cart')
        else:
            return redirect('login')


class RemoveFromCartView(View):

    def post(self, request, product_slug):
        product = get_object_or_404(Products, slug=product_slug)
        cart_item = get_object_or_404(CartItem, product=product, user=request.user)
        cart_item.delete()
        redirect('cart')


class CartView(View):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.total_price() for item in cart_items)
        return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})


class CheckoutView(View):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.total_price() for item in cart_items)
        return render(request, 'cart/checkout.html', {'cart_items': cart_items, 'total': total})




