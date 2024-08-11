from django.contrib import admin
from .models import News, NewsCategory


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ['news_headline', 'id']
    list_display = ['news_headline', 'id']
    ordering = ['-id']


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name', 'id']
    list_display = ['category_name', 'id']
    ordering = ['-id']
