from config import config
import configparser
from init_configuration import  InitConfig

class ConfigParserUtility:
    
    @staticmethod
    def configure():
         parser = configparser.ConfigParser()
         init_config = config.get_setting_from_url()
         parser.read_string(init_config)
         return parser

    @staticmethod
    def read_all_settings():   
         parser = ConfigParserUtility.configure()                 
         InitConfig.Alert.exchange_token = parser["alert"]["exchange_token"]  
         InitConfig.Alert.exchange_token_name = parser["alert"]["exchange_token_name"] 
         InitConfig.Alert.geeks_to_track = parser["alert"]["geeks_to_track"]   
                          
         return InitConfig