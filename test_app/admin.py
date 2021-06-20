from django.contrib import admin

# Register your models here.
from test_app.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)