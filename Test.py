#!/Volumes/Media/project/Crypto_news/cryptoVENV/bin/python3.9

import requests
import json

# api_price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,USDT,BNB,ADA,DOGE,BCH&tsyms=JPY,EUR,USD')
api_price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,BCH&tsyms=JPY,EUR,USD')

api_price_data = json.loads(api_price_request.content)
# print((api_price_data["DISPLAY"]))
currency = "JPY"
# print(api_price_data["DISPLAY"].get(currency)["PRICE"])

for key, value_dict in api_price_data["DISPLAY"].items():
    print(key)
    # print(value_dict.values())
    inside_vlaues = value_dict.get(currency)["PRICE"]
    print("\n\ninside values",type(inside_vlaues),inside_vlaues)
    for currency,curr_values in value_dict.items():
        pass













# # Api call for getting Crypto Prices
# if request.method == "POST":
#     currency = request.POST['currency']
#     price_url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,USDT,BNB,ADA,DOGE,BCH&tsyms="+currency
#     api_price_request = requests.get(price_url)
#     print(currency)
#     api_price_data = json.loads(api_price_request.content)
#     # print(api_price_data)
    
# # else:
# #     currency = "JPY"

#     # print(api_price_data)
# api_share_data =dict()
# # print(api_price_data["DISPLAY"]["BTC"])
# for key,values in api_price_data["DISPLAY"].items():
#     # print(values)
#     api_share_data['key'] = key
#     api_share_data['PRICE'] = values.USD.PRICE
#     print('Price',values.USD.PRICE)
# # print(api_price_data["DISPLAY"])


# # return render(request,'home.html',{"api_news": api_news_data,
# #                                     "api_price":api_price_data,
# #                                     'currency_selected':currency})  