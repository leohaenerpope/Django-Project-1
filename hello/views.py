from django.shortcuts import render

# Create your views here.
import re
from django.utils.timezone import datetime
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page")

def hello_there(request):
    return render(
        request,
        'hello/hello_there.html'
    )