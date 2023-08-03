from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *
from .utils import DataMixin


def index(request):
    return render(request, 'base/index.html')


class TrendProductListView(ListView):
    model = Products
    template_name = 'base/index.html'
    context_object_name = 'products'


class ProductListView(DataMixin, ListView):
    model = Products
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ByCategoryView(DataMixin, ListView):
    model = Products
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = ProductCategory.objects.get(slug=category_slug)
        return Products.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


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
        product = self.get_object()
        context['images'] = ProductImages.objects.filter(product=product)
        return context


class ProductSearchView(DataMixin, ListView):
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Products.objects.filter(name__icontains=self.request.GET.get("search"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))