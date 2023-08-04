from django.contrib import admin
from .models import CartItem, OrderItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'quantity', 'product', 'total_price')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'country', 'address')
