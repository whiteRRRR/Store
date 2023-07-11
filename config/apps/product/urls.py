from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('products/product_list/', ProductListView.as_view(), name='product_list'),
    path('products/product_list/category/<slug:category_slug>/', ByCategoryView.as_view(), name='by_category'),
    path('products/product_list/search', ProductSearchView.as_view(), name='search_product'),
    path('products/product_list/<slug:product_name>/', ProductDetailView.as_view(), name='product_detail'),
]
