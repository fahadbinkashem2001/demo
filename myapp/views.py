from django.shortcuts import render

# Create your views here.

def home(request):
    title = "Home Page"
    context = {"title": title}
    return render(request,"myapp/index.html",context)
