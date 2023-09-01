from django.contrib import admin
from .models import Category, Blog

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Category, CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('title','author', 'published')
    search_fields=('title', 'content', 'author__username', 'categories__name')
    date_hierarchy='published'
    list_filter=('author__username','categories')
admin.site.register(Blog, BlogAdmin)
