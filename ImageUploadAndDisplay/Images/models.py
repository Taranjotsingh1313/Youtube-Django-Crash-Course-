from django.db import models

# Create your models here.
class imageTable(models.Model):
    image = models.ImageField(upload_to='images')
    image_title = models.CharField(max_length=50)
    image_desc = models.CharField(max_length=200)