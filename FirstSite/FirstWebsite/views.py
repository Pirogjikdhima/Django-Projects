from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html",context={'title':'Massively by HTML5 UP'})
def elements(request):
    return render(request,"elements.html",{"title":"Elements Reference - Massively by HTML5 UP"})
def generic(request):
    return render(request,"generic.html",{"title":"Generic Page - Massively by HTML5 UP"})