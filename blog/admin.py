from django.contrib import admin
from .models import Blog, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags'] # 控制表单显示的字段

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

# Register your models here.

admin.site.register(Blog, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)