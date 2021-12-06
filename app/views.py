from django.shortcuts import render
from .models import ColorModel
# Create your views here.

def color_search(request):
    result=ColorModel.objects.all()
    return render(request,'index.html',{'result':result})
