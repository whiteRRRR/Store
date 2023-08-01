from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.db.models import Count
from apps.blog.forms import CommentForm
from apps.blog.models import *
from .utils import *


def index(request):
    return render(request, 'base/index.html')


class BlogListView(CommonContextMixin, ListView):
    model = Blog
    paginate_by = 3
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    ordering = '-date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_context = self.get_common_context_data()
        context.update(common_context)
        return context


class ByCategoryView(CommonContextMixin, ListView):
    model = Blog
    paginate_by = 3
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = BlogCategory.objects.get(slug=category_slug)
        return Blog.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_context = self.get_common_context_data()
        context.update(common_context)
        return context


class ByTagView(CommonContextMixin, ListView):
    paginate_by = 3
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        tag = BlogTags.objects.get(slug=tag_slug)
        return Blog.objects.filter(tags=tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_context = self.get_common_context_data()
        context.update(common_context)
        return context


class BlogSearchView(CommonContextMixin, ListView):
    paginate_by = 3
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        query = self.request.GET.get('search')
        queryset = Blog.objects.filter(title__icontains=query)
        return queryset


class BlogDetailView(CommonContextMixin, FormMixin, DetailView):
    model = Blog
    template_name = 'blog/single-blog.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        blog = self.get_object()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('blog_detail', slug=blog.slug)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()
        context['blogs'] = Blog.objects.all()
        context['comments'] = CommentBlog.objects.filter(blog=blog).annotate(count=Count('blog')).order_by('-count')
        context.update(self.get_common_context_data())
        return context


