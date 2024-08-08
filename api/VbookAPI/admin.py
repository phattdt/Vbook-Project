from django.contrib import admin
from .models import MyModel, POST, LIKE, COMMENT, FOLLOWS

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'profile_picture', 'bio', 'personal_link')

@admin.register(POST)
class POSTAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at', 'updated_at')

@admin.register(LIKE)
class LIKEAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'like_type', 'created_at')

@admin.register(COMMENT)
class COMMENTAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at')

@admin.register(FOLLOWS)
class FOLLOWSAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed')


# Register your models here.
