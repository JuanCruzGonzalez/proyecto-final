from django.shortcuts import render

def inicio(request):
    return render(request, "car/index.html")
# Create your views here.
