from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', TrendProductListView.as_view(), name='homepage'),
    path('products/product_list/', cache_page(300)(ProductListView.as_view()), name='product_list'),
    path('products/product_list/category/<slug:category_slug>/', ByCategoryView.as_view(), name='by_product_category'),
    path('products/product_list/search', ProductSearchView.as_view(), name='search_product'),
    path('products/product_list/<slug:product_name>/', ProductDetailView.as_view(), name='product_detail'),
]
