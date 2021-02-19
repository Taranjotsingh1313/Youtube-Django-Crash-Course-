from django.contrib import admin
from .models import MyFirstModel
# Register your models here.
@admin.register(MyFirstModel)
class Myadmoin(admin.ModelAdmin):
    list_display = ('id','name')