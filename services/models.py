from django.db import models

class Service(models.Model):
    TYPE = (
        ('national','national'),
        ('worldwide','worldwide'),
        ('regional','regional'),

    )
    service_icon = models.CharField(max_length=150)
    service_title = models.CharField(max_length=50,choices = TYPE)
    service_des = models.TextField()


    def __str__(self) :
        return self.service_title

# Create your models here.

