from django.db import models
from apps.user.models import CustomUser
from tinymce.models import HTMLField


class Blog(models.Model):
    """
    Создает модель для блога
    """
    title = models.CharField(max_length=150, verbose_name='Название блога')
    description = HTMLField(verbose_name='Информация о блоге')
    image = models.ImageField(upload_to='blog_image/', verbose_name='Картинка для блога')
    date = models.DateField(auto_now=True, verbose_name='Дата создание')
    slug = models.SlugField(max_length=100, verbose_name='URL адрес блога')
    category = models.ForeignKey('BlogCategory', on_delete=models.PROTECT, verbose_name='Категория')
    tags = models.ManyToManyField('BlogTags', verbose_name='Тэги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class BlogCategory(models.Model):
    """
    Создает модель категорий для блога
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
        Создает модель тэг для блога
    """
    name = models.CharField(max_length=150, verbose_name='Название тэг для блога')
    slug = models.SlugField(max_length=100, verbose_name='URL адрес категорий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class CommentBlog(models.Model):
    """
     Создает модель комментария для блога
     """
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Содержание комментария')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')



