from django.shortcuts import render
import requests
import json

# Create your views here.

# The home screen view function
def home(request):
    
    api_request = requests.get()
    return render(request,'home.html',{})  