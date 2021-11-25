from django.contrib import admin
from .models import Article , File

class ArticleManager(admin.ModelAdmin):
    list_display = ['title', 'name', 'time']
    list_display_links = ['title']
    list_filter = ['classify']
    search_fields = ['title', 'name']

class FileManager(admin.ModelAdmin):
    list_display = ["image_name","article",'image_tag']
    list_display_links = ['image_name',]


admin.site.register(Article, ArticleManager)
admin.site.register(File,FileManager)
# Register your models here.
