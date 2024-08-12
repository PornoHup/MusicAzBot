import os


class Config:

   API_ID = int(os.getenv("API_ID", "26170578"))
   API_HASH = os.getenv("API_HASH", "4ce2d5627427004aed3e0f421e65f0e4")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "7010221401:AAHegnqsvMW_mh0zCQU-TFAgq2qBEMcb0q8")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "nezrinsongbot")
   OWNER_NAME = os.environ.get("OWNER_NAME", "thagiyev") 
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "nezrinlogo")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002168356385"))
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "Nezrin")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/f6c186e3c581a223856c4.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/dc9794139c12507f5eb1c.jpg")    
