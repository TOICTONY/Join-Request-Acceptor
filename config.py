from os import environ

API_ID = int(environ.get("API_ID", "13209296"))
API_HASH = environ.get("API_HASH", "7f94729e7d7f60aff21bb986bc068bd9")
BOT_TOKEN = environ.get("BOT_TOKEN", "7025916558:AAHRZwXYWrElblKN46t8O88ihhgYN8gf-VY")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002029877625"))
ADMINS = int(environ.get("ADMINS", "683443719"))
DB_URI = environ.get("DB_URI", "mongodb+srv://immortal:ironman009@cluster0.yi718.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")
