from django.db.models import Count
from .models import BlogCategory, BlogTags


class CommonContextMixin:
    def get_common_context_data(self):
        common_context = {}
        common_context['categories'] = BlogCategory.objects.all().annotate(count=Count('blog')).order_by('-count')
        common_context['tags'] = BlogTags.objects.all()
        return common_context

