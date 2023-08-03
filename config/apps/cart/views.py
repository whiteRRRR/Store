from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import FormView

from .models import CartItem, OrderItem
from .forms import OrderForm
from .utils import DataMixin


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
        return redirect('cart')


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


class OrderView(DataMixin, FormView):
    form_class = OrderForm
    template_name = 'cart/checkout.html'
    success_url = 'base/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(name='checkout')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        address = form.cleaned_data['address']
        city = form.cleaned_data['city']
        zipcode = form.cleaned_data['zip_code']
        order = OrderItem.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            address=address,
            city=city,
            zipcode=zipcode
        )

        return super().form_valid(form)




