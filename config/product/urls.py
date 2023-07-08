from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_list/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
