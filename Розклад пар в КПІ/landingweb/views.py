from django.shortcuts import render

def index(request):
    return render(request, 'landingweb/home.html')