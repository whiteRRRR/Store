# Generated by Django 4.2.3 on 2023-07-08 06:17

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Названия категории')),
                ('slug', models.SlugField(max_length=100, verbose_name='URL категории')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Названия товара')),
                ('slug', models.SlugField(max_length=100, verbose_name='URL адрес товара')),
                ('description', models.TextField(blank=True, verbose_name='О товаре')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена товара')),
                ('status_of_product', models.CharField(blank=True, max_length=100, verbose_name='Статус товара')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Основное изображение товара')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликована')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='product.productcategory', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=product.models.ProductImages.content_file_name)),
                ('product', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
            options={
                'verbose_name': 'Изображение Товара',
                'verbose_name_plural': 'Изображение Товаров',
            },
        ),
    ]