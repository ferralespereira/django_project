from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# setting admin panel title
title = "Mi django project"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Admin Panel"
