from django.contrib import admin

from .models import Group, Post, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'image',
        'group',
        'author',
        'pub_date'
    )
    list_editable = ('group',)
    search_fields = ('author',)
    list_filter = ('group',)
    list_display_links = ('text',)


admin.site.register(Group)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Follow)
