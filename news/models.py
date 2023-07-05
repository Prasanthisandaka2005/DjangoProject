from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class News(models.Model):
    news_title = models.CharField( max_length=50)
    news_desc=HTMLField()
    news_img=models.FileField(upload_to="news/",max_length=250,null=True,default=None)
    news_slug = AutoSlugField(populate_from ='news_title',unique=True,null=True,default=None) # type: ignore

class Image(models.Model):
    photo=models.ImageField(upload_to="img/",default=None,null=True)