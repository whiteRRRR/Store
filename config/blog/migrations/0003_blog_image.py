# Generated by Django 4.2.3 on 2023-07-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_tag_blog_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=2, upload_to='blog_image/', verbose_name='Картинка для блога'),
            preserve_default=False,
        ),
    ]
