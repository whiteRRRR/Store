from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('blog_list/', cache_page(300)(BlogListView.as_view()), name='blog_list'),
    path('blog_list/search', BlogSearchView.as_view(), name='blog_search'),
    path('blog_list/category/<slug:category_slug>/', ByCategoryView.as_view(), name='by_category'),
    path('blog_list/tags/<slug:tag_slug>/', ByTagView.as_view(), name='by_tag'),
    path('blog_list/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail')
]