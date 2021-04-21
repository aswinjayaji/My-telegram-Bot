import random 
from datetime import datetime
import urllib3
import json
# BTC, ETH, XRP, BCH, ADA, XLM, NEO, LTC, EOS, XEM, IOTA, DASH, XMR, TRX, ICX, ETC,
# QTUM, BTG, LSK, USDT, OMG, ZEC, SC, ZRX, REP, WAVES, MKR, DCR, BAT, LRC, KNC, 
# BNT, LINK, CVC, STORJ, ANT, SNGLS, MANA, MLN, DNT, NMR, DOT, DAI, UNI, ATOM, 
# GRT, XTZ, FIL, NANO, WBTC, BSV, DOGE, USDC, OXT, ALGO, BAND, BTT, FET, KAVA, 
# PAX, PAXG, REN, AAVE, YFI, NU

cryptos=["BTC","ETH","NANO","DOGE"]
coinName=random.choice(cryptos)
print(coinName)

now=datetime.now()
ddmmyyht=str(now.strftime("%Y-%m-%dT%H:%M"))
print(ddmmyyht)
http = urllib3.PoolManager()
# https://production.api.coindesk.com/v2/price/values/DOGE?start_date=2020-04-21T22:12&end_date=2020-04-21T22:12&ohlc=true
req = http.request('GET','https://production.api.coindesk.com/v2/price/values/DOGE?start_date=2021-04-21T22:20&end_date=2021-04-21T22:47&ohlc=true')
# json.loads(req.data.decode('utf-8'))
data=json.loads(req.data.decode('utf-8'))
print(json.dumps(data,indent=4))
