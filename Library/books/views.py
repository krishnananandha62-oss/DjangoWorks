from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def addbook(request):
    return render(request,'addbook.html')
def booklist(request):
    return render(request,'booklist.html')