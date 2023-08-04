from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from .models import CartItem, OrderItem
from .forms import OrderForm, UpdateCartItemForm
from ..product.models import Products


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


class UpdateCartItemsView(View):
    def post(self, request):
        for key, quantity in request.POST.items():
            if key.startswith('quantity_'):
                cart_item_id = key.split('_')[1]
                cart_item = get_object_or_404(CartItem, id=cart_item_id, user=self.request.user)
                cart_item.quantity = int(quantity)
                cart_item.save()
        return redirect('cart')


class OrderView(FormView):
    form_class = OrderForm
    template_name = 'cart/checkout.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = CartItem.objects.filter(user=self.request.user)
        total = sum(item.total_price() for item in cart_items)
        context['cart_items'] = cart_items
        context['total'] = total
        return context

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        address = form.cleaned_data['address']
        city = form.cleaned_data['city']
        country = form.cleaned_data['country']
        zipcode = form.cleaned_data['zipcode']
        order = OrderItem.objects.create(
            user=self.request.user,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            address=address,
            country=country,
            city=city,
            zipcode=zipcode
        )
        return super().form_valid(form)





