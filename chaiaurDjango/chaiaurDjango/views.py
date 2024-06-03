from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("<h1>Hello, world. You are at chai aur Django Home page<h1>")
    return render(request,'website/index.html')


def about(request):
    # return HttpResponse("Hello, world. You are at chai aur Django about page")
    return render(request,'website/about.html')
    


def contact(request):
    # return HttpResponse("Hello, world. You are at chai aur Django contact us page")
    return render(request,'website/contact.html')

def services(request):
    return render(request, 'website/services.html')
