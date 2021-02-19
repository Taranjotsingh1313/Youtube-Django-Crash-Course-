from django.shortcuts import render
from .models import imageTable
from django.contrib import messages
# Create your views here.
# -------------------This View Upload Image and Display It As Well -----------
def imageindex(request):
    data = imageTable.objects.all()
    if request.method == 'POST':
        title = request.POST['imagetitle']
        desc = request.POST['imagedesc']
        images = request.FILES['imagez']
        modelsave = imageTable(image=images,image_title=title,image_desc=desc)
        modelsave.save()
        messages.success(request,'Image Uploaded Successfully')
        return render(request,'Images/index.html',{'data':data})
    return render(request,'Images/index.html',{'data':data})