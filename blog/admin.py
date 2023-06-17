from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


# Blog text fields will include Summernote text editor
# And show Post title, slug, status and created on in the admin view
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    search_fields = ['title', 'content']
    list_display = ('title', 'slug', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on',)
    search_fields = ['name', 'email', 'body']


admin.site.register(Category)
