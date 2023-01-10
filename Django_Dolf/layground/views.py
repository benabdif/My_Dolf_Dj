from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# get the resuest -> response


# This is what I did in this

def say_hello(request):
    return HttpResponse("Hello world From Dolf...")



