from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    list_filter = ("created_on", 'title', 'article_description')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'created')
    list_filter = ('created',)
    search_fields = ('name', 'email', 'content')
