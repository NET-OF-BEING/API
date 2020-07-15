import base64, hashlib, hmac, time, json, config, pprint,subprocess
from urllib.request import urlopen, Request

base_url = 'https://api.btcmarkets.net'

def request(action, key, signature, timestamp, path, data):
    header = {
        'Accept': 'application/json',
        'Accept-Charset': 'UTF-8',
        'Content-Type': 'application/json',
        'apikey': key,
        'timestamp': timestamp,
        'signature': signature,
    }

    http_request = Request(base_url + path, data, header)
    pprint.pprint(base_url, path, data, header)
    if action == 'post':
        response = urlopen(http_request, data)
    else:
        response = urlopen(http_request)
    return json.loads(response.read())

def get_request(key, secret, path):
    nowInMilisecond = str(int(time.time() * 1000))
    stringToSign = path + "\n" + nowInMilisecond + "\n"

    presignature = base64.b64encode(hmac.new(secret, stringToSign.encode('utf-8'), digestmod=hashlib.sha512).digest())
    signature = presignature.decode('utf8')
    return request('get', key, signature, nowInMilisecond, path, None)

def post_request(key, secret, path, postData):

    nowInMilisecond = str(int(time.time() * 1000))
    stringToSign = path + "\n" + nowInMilisecond + "\n" + postData

    signature = base64.b64encode(hmac.new(secret, stringToSign.encode('utf-8'), digestmod=hashlib.sha512).digest())

    return request('post', key, signature, nowInMilisecond, path, postData)


class BTCMarkets:

    def __init__(self, key, secret):
        self.key = key
        self.secret = base64.b64decode(secret)

    def open_orders(self):
        return get_request(self.key, self.secret, '/order/open')
   
    def order_details(self):
        return get_request(self.key, self.secret, '/order/detail')
    
    def open_all_orders(self):
        return open_orders(self.key, self.secret, '/v2/order/open[/{instrument}/{currency}')
    
    def account_balance(self):
        return get_request(self.key, self.secret, '/account/balance')
    
    def order_history(self):
        subprocess.call('clear')
        instrument = input("Enter coin ticker: ")
        currency = input("Enter currency: ")
        return get_request(self.key, self.secret, '/v2/order/history/{instrument}/{currency}')
    
    def trade_history(self):
        subprocess.call('clear')
        instrument = input("Enter coin ticker: ")
        currency = input("Enter currency: ")
        return get_request(self.key, self.secret, '/v2/order/trade/history/{instrument}/{currency}')


if __name__ == "__main__":
    key = config.api_key
    secret = config.private_key    
    print(key, secret)
    client = BTCMarkets(key, secret)

    print ('''
   ________  _________  ________          _____ ______   ________  ________  ___  __    _______  _________  ________      
  |\   __  \|\___   ___\\   ____\        |\   _ \  _   \|\   __  \|\   __  \|\  \|\  \ |\  ___ \|\___   ___\\   ____\     
  \ \  \|\ /\|___ \  \_\ \  \___|        \ \  \\\__\ \  \ \  \|\  \ \  \|\  \ \  \/  /|\ \   __/\|___ \  \_\ \  \___|_    
   \ \   __  \   \ \  \ \ \  \            \ \  \\|__| \  \ \   __  \ \   _  _\ \   ___  \ \  \_|/__  \ \  \ \ \_____  \   
    \ \  \|\  \   \ \  \ \ \  \____        \ \  \    \ \  \ \  \ \  \ \  \\  \\ \  \\ \  \ \  \_|\ \  \ \  \ \|____|\  \  
     \ \_______\   \ \__\ \ \_______\       \ \__\    \ \__\ \__\ \__\ \__\\ _\\ \__\\ \__\ \_______\  \ \__\  ____\_\  \ 
      \|_______|    \|__|  \|_______|        \|__|     \|__|\|__|\|__|\|__|\|__|\|__| \|__|\|_______|   \|__| |\_________\
                                                                                                              \|_________|
                                                                                                                          
                                                                                                                          ''')
    print("---------------------------------")
    print("Select an option:")
    print("---------------------------------\n")
    print("1. Trade History")
    print("2. Account Balance")
    print("3. Order History")
    print("4. Cancel Order")
    print("5. Order Details")
    print("6. Cancel Sell Order")
    print("7. Cancel Buy Order")
    print("8. Get Orders by ID")
    print("9. Cancel Orders by ID")
    print("a. List Trades")
    print("0. Request Withdraw")
    print("o. List Withdraws")
    print("h. Get withdraw by ID")
    print("b. List Deposits")
    print("g. List Withdraw/Deposits")
    print("r. Get Deposit Address")
    print("p. Place Sell Order")
    print("q. Quit\n\n")
    print("----------------------------------\n")

    #menuchoices = {'1':client.trade_history,'2':client.account_balance,'3':client.order_history, '5':client.order_details}
    acc = client.account_balance()
    pprint.pprint(acc)
    ret = menuchoices[input("Option: ")]()
    if ret is None:
        print("Please enter a valid menu choice!")
    menuchoices['q']()

    pprint.pprint(client.order_detail([1234, 213456]))
    pprint.pprint(client.order_create('AUD', 'LINK', 100000000, 100000000, 'Bid', 'Limit', '1'))
#pprint.pprint(client.account_balance())
#print(dir(client))
#history =  client.trade_history('LINK','AUD')
#order1 =  client.orderHistory()
#pprint.pprint(order1)
#pprint.pprint(client.order_details())

print('''
    

    ------------------------------------------------------------------------------------------------------------ 
    Trade history XRP
    ------------------------------------------------------------------------------------------------------------
    ''')

pprint.pprint(client.order_history())
for key in history:
    print (key,'==>',history[key]/n)
    if isinstance(history[key], Iterable):
        for item in history[key][item]:
            print(item,'\n')
            pprint.pprint(client.order_detail([1234, 213456]))
            pprint.pprint(client.order_create('AUD', 'LINK', 100000000, 100000000, 'Bid', 'Limit', '1'))

print('''


    ------------------------------------------------------------------------------------------------------------
	Account Balance
    ------------------------------------------------------------------------------------------------------------
''')
balance=client.account_balance()
for item in range(len(balance)):
    for category in balance[item]:
        cat = str(category)
        value=str(balance[item][cat])
        print(cat, "==>" ,value)
        pprint.pprint(balance)
        pprint.pprint('Currency: ',balance['currency'])
        pprint.pprint('Balance: ',balance['balance'])

	#print(colors in range[256])
	#for i in range(256):
	#    print(color('Color #%d' % i, fg=i))
	#print(color("TEST", fg=10))

    print('''
	-------------------------------------------------------------------------------------------------------------
	Asking/Selling bids
	-------------------------------------------------------------------------------------------------------------
    ''')

    pprint.pprint(client.get_market_tick('XRP','AUD'))
    pprint.pprint(client.get_market_tick('BTC','AUD'))
    pprint.pprint(client.get_market_tick('LTC','AUD'))
    pprint.pprint(client.get_market_tick('OMG','AUD'))
    pprint.pprint(client.get_market_tick('ETC','AUD'))
