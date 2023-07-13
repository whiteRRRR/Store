from .models import BlogCategory, BlogTags


class CommonContextMixin:
    def get_common_context_data(self):
        common_context = {}
        common_context['categories'] = BlogCategory.objects.all()
        common_context['tags'] = BlogTags.objects.all()
        return common_context
