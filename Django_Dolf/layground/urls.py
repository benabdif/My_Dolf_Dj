from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.say_hello),
    path('about/', views.my_hi)
    
    
    
    
]
