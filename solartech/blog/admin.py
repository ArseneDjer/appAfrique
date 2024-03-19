from django.contrib import admin
from .models import Article, ForumPost

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    search_fields = ('title', 'content')
    ordering = ('-date_published',)

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_posted')
    search_fields = ('title', 'content', 'user__username')
    ordering = ('-date_posted',)
