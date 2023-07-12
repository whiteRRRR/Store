from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.db.models import Count
from apps.blog.models import *


def index(request):
    return render(request, 'base/index.html')


class BlogListView(ListView):
    model = Blog
    paginate_by = 1
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = BlogCategory.objects.all()
        context['tags'] = BlogTags.objects.all()
        return context


class ByCategoryView(ListView):
    model = Blog
    paginate_by = 1
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = BlogCategory.objects.get(slug=category_slug)
        return Blog.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all()
        context['tags'] = BlogTags.objects.all()
        return context


class ByTagView(ListView):
    paginate_by = 1
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        tag = BlogTags.objects.get(slug=tag_slug)
        return Blog.objects.filter(tags=tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all()
        context['tags'] = BlogTags.objects.all()
        return context



class BlogSearchView(ListView):
    paginate_by = 1
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        query = self.request.GET.get('search')
        queryset = Blog.objects.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['search'] = self.request.GET.get('search')
        context['categories'] = BlogCategory.objects.all()
        context['tags'] = BlogTags.objects.all()
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/single-blog.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = BlogTags.objects.all()
        context['blogs'] = Blog.objects.all()
        context['categories'] = BlogCategory.objects.annotate(count=Count('blog')).order_by('-count')
        return context



