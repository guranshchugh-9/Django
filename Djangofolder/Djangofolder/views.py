from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello. how are you?")
    # return render(request,'index.html')
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/index2.html')

def contact(request):
    return HttpResponse("bro bro bro aap?")


