from django.db import models
from apps.product.models import Products
from apps.user.models import CustomUser


class CartItem(models.Model):
    product = models.ForeignKey('product.Products', on_delete=models.CASCADE)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price
    