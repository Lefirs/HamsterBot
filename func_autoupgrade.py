from imports import *
from settings import token, user_agent




def auto_upgrade():
    timestamp = int(datetime.datetime.timestamp(datetime.datetime.now()))
    levels = []
    max_level = 0
    balance_for_buy = False
    price = 0
    list_upgrade = json.loads(requests.post(url='https://api.hamsterkombat.io/clicker/upgrades-for-buy', headers={"Authorization": token, "User-Agent": user_agent}).content.decode('utf-8'))["upgradesForBuy"]
    #get_max_lvl start
    for i in list_upgrade:
        for key, value in i.items():
            if key == 'level':
                levels.append(value)
    max_level = max(levels)
    #get_max_lvl end
    for i in list_upgrade:
        for key, value in i.items():
            if key == "id":
                id = value
            if key == "price":
                price = int(value)
            if key == "level":
                level = int(value)
        balance = int(json.loads(requests.post(url='https://api.hamsterkombat.io/clicker/sync', headers={"Authorization": token, "User-Agent": user_agent}).content.decode('utf-8'))["clickerUser"]["balanceCoins"])
        if level < max_level:
            if price < balance:
                os.system('cls')
                print('Balance: ', balance)
                requests.post(url='https://api.hamsterkombat.io/clicker/buy-upgrade', headers={"Authorization": token, "User-Agent": user_agent}, json={"timestamp": timestamp, "upgradeId": id})
                print(id, '\n', price, '\n', level, 'Buyed')
                time.sleep(1)

#auto_upgrade()

