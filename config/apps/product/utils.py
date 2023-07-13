from .models import Products, ProductCategory


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = ProductCategory.objects.all()

        context['search'] = self.request.GET.get('search')
        context['categories'] = categories

        return context