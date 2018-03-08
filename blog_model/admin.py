# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from blog_model.models import Tag,Article,Category,Comment,Links

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass

@admin.register(Article)
class Article(admin.ModelAdmin):
    pass

@admin.register(Category)
class Category(admin.ModelAdmin):
    pass

@admin.register(Comment)
class Conment(admin.ModelAdmin):
    pass

@admin.register(Links)
class Links(admin.ModelAdmin):
    pass