from django.db import models


class Blog(models.Model):
    """
    Создает класс для блога
    """
    title = models.CharField(max_length=150, verbose_name='Название блога')
    description = models.TextField(blank=True, verbose_name='Информация о блоге')
    image = models.ImageField(upload_to='blog_image/', verbose_name='Картинка для блога')
    date = models.DateField(auto_now=True, verbose_name='Дата создание')
    slug = models.SlugField(max_length=100, verbose_name='URL адрес блога')
    category = models.OneToOneField('BlogCategory', on_delete=models.PROTECT, verbose_name='Категория')
    tag = models.ManyToManyField('BlogTags', verbose_name='Тэги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class BlogCategory(models.Model):
    """
    Создает категорий для блога
    """
    name = models.CharField(max_length=150, verbose_name='Название категорий блога')
    slug = models.SlugField(max_length=100, verbose_name='URL адрес категорий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'


class BlogTags(models.Model):
    """
        Создает тэг для блога
    """
    name = models.CharField(max_length=150, verbose_name='Название тэг для блога')
    slug = models.SlugField(max_length=100, verbose_name='URL адрес категорий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'




