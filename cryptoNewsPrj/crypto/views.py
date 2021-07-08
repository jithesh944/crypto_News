from django.shortcuts import render
import requests
import json

# Create your views here.

# The home screen view function
def home(request):
    # Api call for getting Crypto Prices
    api_price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,USDT,BNB,ADA,DOGE,BCH&tsyms=USD,JPY')
    api_price_data = json.loads(api_price_request.content)


    # API call fro getting crypto news
    api_news_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api_news_data = json.loads(api_news_request.content)


    return render(request,'home.html',{"api_news": api_news_data,"api_price":api_price_data})  