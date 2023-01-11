from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# get the resuest -> response


# This is what I did in this

def say_hello(request):
    # we can add dic in this open
    return render(request, 'hello.html',{'name':['1','Hello','2']})
    
    


# This is the scound page 
def my_hi(request):
    return render(request,'about.html')