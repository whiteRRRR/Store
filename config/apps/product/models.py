import os

from django.db import models
from tinymce.models import HTMLField


class Products(models.Model):
    """
    Создает модель класса продуктов
    """
    name = models.CharField(max_length=150, verbose_name='Названия товара')
    slug = models.SlugField(max_length=100, verbose_name='URL адрес товара')
    description = HTMLField(blank=True, verbose_name='О товаре')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена товара')
    status_of_product = models.CharField(blank=True, max_length=100, verbose_name='Статус товара')
    image = models.ImageField(upload_to="product_image/", verbose_name='Основное изображение товара')
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')
    category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductCategory(models.Model):
    """
    Создает модель класса категории продуктов
    """
    name = models.CharField(max_length=100, verbose_name='Названия категории')
    slug = models.SlugField(max_length=100, verbose_name='URL категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'


class ProductImages(models.Model):
    """
    Создает модель класса изображений продукта
    """

    def content_file_name(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.product.name, ext)
        return os.path.join('other_image', filename)

    product = models.ForeignKey('Products', on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to=content_file_name)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Изображение Товара'
        verbose_name_plural = 'Изображение Товаров'
