from curses import ALL_MOUSE_EVENTS
import pandas as pd
import requests
import threading


stock_price = int(0)
share_count = int(0)

balance = int(input('Enter balance: '))
print('Balance = ', balance)

def get_latest_updates(*symbol):
    global stock_price
    for i in symbol:
        ticker = i
        api_key = 'sk_dd827c5d28154709853a3f18c87b7246'
        url = f'https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={api_key}'
        df = requests.get(url).json()
        attributes = ['latestPrice']
        for i in attributes:
            stock_price = format(df[i])
            return float(stock_price)


def call_get_updates():
    get_latest_updates('AAPL')
    threading.Timer(1.0, call_get_updates).start()
    
call_get_updates()

action = input('b for buy, s for sell, c for check price, q for check amount of shares, e for equity, cap for capital')



def buy(amount):
    
    global share_count
    global balance
    balance = float(balance)
    share_count += amount
    buyprice = amount * stock_price
    buyprice = float(buyprice)
    balance -= buyprice
    print('Amount of shares = ', amount, 'Balance = ', balance)
    return share_count
    return balance 


    

if(action == 'b'):
    amount = int(input('Enter amount '))
    buy(amount)
    

