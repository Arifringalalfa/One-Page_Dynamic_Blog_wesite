from django.contrib import admin
from .models import *


class TagTublarInlines(admin.TabularInline):
    model = Tag


class PostAdmin(admin.ModelAdmin):
    inlines = [TagTublarInlines]
    list_display = ['title', 'author', 'date','section', 'status', 'Main_post']
    list_editable =['status', 'section', 'Main_post']
    search_fields =['title','author','section']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
