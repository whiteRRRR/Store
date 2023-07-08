from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from blog.models import *


def index(request):
    return render(request, 'base/index.html')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/single-blog.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = BlogTags.objects.all()
        return context



