from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'text',)
    list_filter = ('title', 'created', 'text', )
    search_fields = ('title', 'created', 'text', )

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display =('text', 'post', 'logname')
    list_filter = ('text', 'post', 'logname')
    search_fields = ('text', 'post', 'logname')
