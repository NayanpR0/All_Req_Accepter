from os import environ
import os

API_ID = int(environ.get('API_ID', "12897895"))
API_HASH = environ.get('API_HASH', "66009ef52a2da9cea6a7015e59b556ca")
BOT_TOKEN = environ.get('BOT_TOKEN', "6217851267:AAF71ZbS-5ZRF6BPkYGsG6p8cbbJL2-evnI")
DB_URI = environ.get('DB_URI', "mongodb+srv://tgprem:tgprem@cluster0.nbdny9o.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get('DB_NAME', 'Cluster0')
