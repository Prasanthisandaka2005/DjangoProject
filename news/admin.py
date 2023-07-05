from django.contrib import admin
from news.models import News,Image

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title','news_desc','news_img')


class ImageAdmin(admin.ModelAdmin):
    display= ['id','photo']

admin.site.register(News,NewsAdmin)
admin.site.register(Image,ImageAdmin)
