from settings import *
from imports import *

def auto_tap():
    availableTaps = int(json.loads(requests.post(url='https://api.hamsterkombat.io/clicker/sync', headers=headers).content.decode('utf-8'))['clickerUser']['availableTaps'])
    requests.post(url='https://api.hamsterkombat.io/clicker/tap', headers=headers, json={"availableTaps": availableTaps, "count": availableTaps, "timestamp": int(datetime.datetime.timestamp(datetime.datetime.now()))})


#autotap()