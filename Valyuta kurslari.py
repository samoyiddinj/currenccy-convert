import requests
import json
currency_type = int(input("1. USD>UZS\n2. UZS>USD\n3.USD>RUB: "))
# to_currency = str(input("Enter in the currency you'd like to convert to: ")).upper()
amount = float(input("Enter in the amount of money: "))

url = "https://nbu.uz/uz/exchange-rates/json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    calculate = 0
    for i in data:
        print(i)
        if currency_type == 1:
            if i['code'] == 'USD':
                calculate = amount * float(i['cb_price'])
                print(f"{amount} USD : {calculate} UZS")
        elif currency_type == 2:
            if i['code'] == 'USD':
                calculate = amount / float(i['cb_price'])
                print(f"{amount} UZS : {calculate} USD")
        elif currency_type == 3:
            if i['code'] == 'USD':
                a  = amount * float(i['cb_price'])
                for j in data:
                    if j['code'] == 'RUB':
                        calculate = a / float(j['cb_price'])
                        print(f"{amount} USD : {calculate} RUB")
                        break






else:
    print("sayt vaqtincha ishlamayapti")
# data = response.json()
# print(response.status_code, data, type(data), len(data))