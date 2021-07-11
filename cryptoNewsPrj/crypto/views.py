from django.shortcuts import render
import requests
import json
from django.http import HttpResponse, response
import os.path  


# Create your views here.

# The home screen view function
def home(request):
    currency ="JPY"
    api_price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,USDT,BNB,ADA,DOGE,BCH&tsyms=JPY')
    api_price_data = json.loads(api_price_request.content)

    # Api call for getting Crypto Prices
    if request.method == "POST":
        currency = request.POST['currency']
        price_url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,USDT,BNB,ADA,DOGE,BCH&tsyms="+currency
        api_price_request = requests.get(price_url)
        api_price_data = json.loads(api_price_request.content)

    api_share_data =dict()
    for key,values in api_price_data["DISPLAY"].items():
        api_share_data[key] = values.get(currency)

    # API call fro getting crypto news
    api_news_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api_news_data = json.loads(api_news_request.content)


    return render(request,'home.html',{"api_news": api_news_data,
                                        "api_price":api_share_data,
                                        'currency_selected':currency})  


def prices(request):

    if request.method == "POST":
        quote = request.POST['quote']
        return render(request,'prices.html',{})
    
    else:
        return render(request,'prices.html',{})