from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *


def index(request):
    return render(request, 'base/index.html')


class ProductListView(ListView):
    model = Products
    template_name = 'product/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Products.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Products
    template_name = 'product/single-product.html'
    context_object_name = 'products'
    slug_url_kwarg = 'slug'


# def single_product(request, slug):
#     product = Products.objects.get(slug=slug)
#     context = {'products': product}
#     return render(request, 'product/single-product.html', context=context)


