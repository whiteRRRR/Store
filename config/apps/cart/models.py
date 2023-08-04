from django.db import models

from apps.product.models import Products
from apps.user.models import CustomUser


class CartItem(models.Model):
    """Модель для корзины"""
    product = models.ForeignKey('product.Products', on_delete=models.CASCADE)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price

    class Meta:
        verbose_name = 'Корзина товара пользователя'
        verbose_name_plural = 'Корзина товаров пользователя'


class OrderItem(models.Model):
    """Модель для оформления заказа"""
    user = models.ForeignKey('user.CustomUser', on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Оформленный заказ'
        verbose_name_plural = 'Оформленные заказы'
