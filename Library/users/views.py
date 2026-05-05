from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def registerview(request):
    return render(request,'registerview.html')
def loginview(request):
    return render(request,'loginview.html')
def logoutview(request):
    return HttpResponse("logout")