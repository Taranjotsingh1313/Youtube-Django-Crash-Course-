from django.contrib import admin
from .models import imageTable
# Register your models here.
@admin.register(imageTable)
class ImageTable(admin.ModelAdmin):
    list_display = ('id','image_title')