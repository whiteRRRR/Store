from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *


def index(request):
    return render(request, 'base/index.html')


class ProductListView(ListView):
    model = Products
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


class ByCategoryView(ListView):
    model = Products
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = ProductCategory.objects.get(slug=category_slug)
        return Products.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Products
    template_name = 'product/single-product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_name'

    def get_queryset(self):
        product_name = self.kwargs['product_name']
        return Products.objects.filter(slug=product_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context









