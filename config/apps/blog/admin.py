from django.contrib import admin
from .models import *


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    display_tags.short_description = 'Тэги'
    list_display = ('title', 'category', 'display_tags', 'date')
    prepopulated_fields = {"slug": ('title',)}


admin.register(BlogCategory)
admin.site.register(BlogTags)