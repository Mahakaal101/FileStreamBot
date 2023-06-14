# (c) @AvishkarPatil | @EverythingSuckz

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID', '16445683'))
    API_HASH = str(getenv('API_HASH', 'd0852e13eee2389ff2d9183b00649547'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6213184839:AAHXx24g0MV9pg-ntJii6gzdCJtYN6yoDro'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'AviStreamBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001813214601'))
    PORT = int(getenv('PORT', 445))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '34.230.4.214'))
    OWNER_ID = int(getenv('OWNER_ID', '5152847809'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://sonukumarkrbbu61:52EO6iqQL1diHODm@db.op4pluq.mongodb.net/?retryWrites=true&w=majority-1001813214601'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '500'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001296894100")).split()))
