from django.contrib import admin
from .models import Category, Author, Post, Comment, Reply, Recipe, Topic

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Recipe)
admin.site.register(Topic)