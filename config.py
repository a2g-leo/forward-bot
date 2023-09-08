import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "29310987"))
    API_HASH = os.environ.get("API_HASH", "336c28913a45587a4c10af8cd620b68f")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6403785146:AAFZrpcYWKHjsDIkGvFBZZYkxDgJcKi1ZeM")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6515901556")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://fast:leofast@cluster0.u8srkac.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "1BVtsOLEBuzeucprO-byVzWpPDQbIIxc3YjVLdajR80qJJIjeHWuIGH_4lw88uWaQBjPXGl-Hf-oBJUdmvQLBsEz7Mz_kvOFX2UJY4SI3hwfEdJ6HMy-JaaFoFkmCEvNHBqDgOCWNDu1eZ3PvwVAsPj2-c8F4mhnlRI-rGCOWYDjlc9NNsZTOG3oqye664RK2pneAUQublxtGjwW0SSJeLvAg3slJqYrTEdBUmm3VgKtbi1EXpkquiKHjpB2geIFHnLtdZoOSAFW7MW816OmlMaUJaqkXXqy331INy8eDDmQDwno7-SXbdpUAqFwm-aQIC7YySnYRDpMsaON0PNNafBAhLTuCrHc=")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001918596333"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "uniquifyleo_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
