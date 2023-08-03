from apps.product.models import Products


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        products = Products.objects.all()
        context['products'] = products

        return context