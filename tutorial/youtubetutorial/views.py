from django.shortcuts import render
from django.http import HttpResponse
from .models import MyFirstModel
# Create your views here.
def index(request):
    name = 'THIS IS CRAWLER TUTORIAL OF DJANGO THIS COMES FROM OUR DJANGO VIEWS'
    Tutoal = 'DJANgo'
    database = MyFirstModel.objects.all()
    context = {'name':name,'tut':Tutoal,'data':database}
    return render(request,'youtubetutorial/index.html',context)