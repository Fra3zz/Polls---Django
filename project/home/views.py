from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    ret = HttpResponse("Home page")
    return ret

def main(request):
    ret = render(request, "home/main.html")
    return ret