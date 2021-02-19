from django.urls import path
from .import views

urlpatterns = [
    path('',views.imageindex,name='imageindex'),
]