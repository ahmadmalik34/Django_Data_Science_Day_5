from django.contrib import admin
from .models import Author, Category, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'user']
    search_fields = ['name', 'email']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['created_at', 'author', 'categories']
    readonly_fields = ['created_at', 'updated_at']
    filter_horizontal = ['categories']