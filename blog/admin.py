from django.contrib import admin
from .models import Category, Blog

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Category, CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('title','author', 'published')
admin.site.register(Blog, BlogAdmin)
