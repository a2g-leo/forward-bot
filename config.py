import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "29310987"))
    API_HASH = os.environ.get("API_HASH", "336c28913a45587a4c10af8cd620b68f")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6403785146:AAFZrpcYWKHjsDIkGvFBZZYkxDgJcKi1ZeM")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6515901556")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://fast:leofast@cluster0.u8srkac.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'fast')
    SESSION = os.environ.get("SESSION", "1BVtsOJIBu8LWKvj7kPH5LlCEFvlBJKKYMYFanU5-O10w8B3IcuRhydRZpyaDX4n3iqK_Dq2DpTkHj2Uw6M-qVjckHvOWHigQaKzp9QyrpJ8gBnob2EjQNPLT45g9WZRIdVeadB1tdLtapdjxLG2__PI2ZNG8tUHDo8vYgLn10A751bV236TLboOQJJfgnenOnRMN8pGxA0PZbOtXer6FxppPMI0PgHrlJEAygfvikq-lYkKSdtrt5Pb8BRTUkqCmNBMW1pUQuU8PktAvhqiYZcy4dWPXaaR6iExv-BcRV6DoOjj7GhiPpqPd01EEYTULvBDMJVjzf9dttLmRJ5V79mVEHhx488M=")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001918596333"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "uniquifyleo_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
