from django.contrib import admin
from .models import Category
from .models import News
from .models import Comment


admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display= ('title','category','add_time')

admin.site.register(News,AdminNews)

class AdminComment(admin.ModelAdmin):
    list_display= ('news','email','comment','status')

admin.site.register(Comment,AdminComment)