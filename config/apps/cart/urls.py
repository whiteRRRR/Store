from django.urls import path
from .views import *

urlpatterns = [
    path('cart_list/', CartView.as_view(), name='cart'),
    path('add/<slug:product_slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<slug:product_slug>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart/update/', UpdateCartItemsView.as_view(), name='update_cart_items'),
    path('checkout/', OrderView.as_view(), name='checkout')

]
