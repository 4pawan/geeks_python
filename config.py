import requests
class config:
   api_key = 'XXXX'
   username = 'XXXX'
   pwd = 'XXXXX'
   token = "XXXXXX"
   azure_storage_connection_string ="XXXXXXX"
   time_zone ="Asia/Kolkata"
   setting_url ="XXXXX"

   @staticmethod
   def get_setting_from_url():          
       response_data =  requests.get(config.setting_url) 
       return response_data.text 