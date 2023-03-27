import datetime, pandas, requests, yfinance
import mplfinance as mpf
from alpaca_trade_api.stream import Stream
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
from getpass import getpass
from config import KEY, API_ALPACA, SECRET

BASE_URL = API_ALPACA
API_KEY = KEY
SECRET_KEY = SECRET

api = REST(key_id=API_KEY, secret_key=SECRET_KEY, base_url=BASE_URL)

news = api.get_news('TSLA')

print(news)