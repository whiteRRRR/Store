from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_list/category/<slug:category_slug>/', ByCategoryView.as_view(), name='by_category'),
    path('product_list/<slug:product_name>/', ProductDetailView.as_view(), name='product_detail'),

]
