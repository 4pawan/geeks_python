import pandas as pd
from smartConnect import SmartConnect
import pyotp
from datetime import datetime as dt
from config import config
import pytz
from blob_util import BlobUtility as bu 

api_key = config.api_key
username = config.username
pwd = config.pwd
token = config.token
      
#print(pytz.all_timezones)
class Geeks:    
     @staticmethod
     def generate_geeks_report(dtvalue):        
        smartApi = SmartConnect(api_key)
        totp = pyotp.TOTP(token).now()
        smartApi.generateSession(username, pwd, totp)
        option_input = {"name": "HDFCLIFE","expirydate": "29AUG2024"}
        options_result = smartApi.optionGreek(option_input) 
        stock_live_price= smartApi.ltpData(exchange ="NSE",tradingsymbol="HDFCLIFE", symboltoken="467")

        if options_result["message"] == "SUCCESS":
            options_data = options_result["data"]    
            df = pd.DataFrame(options_data)
            df['stockPrice'] = stock_live_price["data"]["ltp"]
            tz = pytz.timezone(config.time_zone)
            date_time_now = dt.now(tz)
            df['date'] = date_time_now.date().strftime("%d-%m-%Y")
            df['time'] = date_time_now.time().strftime("%H:%M")
            data = df.to_csv()
            bu.add_logging_to_azure_blob(data)
