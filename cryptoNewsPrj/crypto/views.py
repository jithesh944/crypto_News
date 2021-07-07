from django.shortcuts import render
import requests
import json,pprint

# Create your views here.

# The home screen view function
def home(request):
    
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api_data = json.loads(api_request.content)
    # print(api_data)
    # api_data_pprint = pprint.pprint(api_data)

    return render(request,'home.html',{"api": api_data})  