import time

from imports import *
from settings import *
from func_autoupgrade import auto_upgrade
from func_autotap import auto_tap
from func_code import code_write
from auto_sync import  auto_sync

def input_command():
    command = input("Write command num: ")
    return command

def start(eupgrade, etap):
    aupgrade = eupgrade
    atap = etap
    tupgrade = None
    ttap = None
    if aupgrade == True:
        tupgrade = 'Activated'
    else:
        tupgrade = 'Deactivated'

    if atap == True:
        ttap = 'Activated'
    else:
        ttap = 'Deactivated'
    print('start')
    os.system('cls')
    os.system("title HamsterKombat Bot")
    balance = int(json.loads(requests.post(url='https://api.hamsterkombat.io/clicker/sync', headers=headers).content.decode('utf-8'))['clickerUser']['balanceCoins'])
    print(r"""
              _______  _______  _______ _________ _______  _______ 
    |\     /|(  ___  )(       )(  ____ \\__   __/(  ____ \(  ____ )
    | )   ( || (   ) || () () || (    \/   ) (   | (    \/| (    )|
    | (___) || (___) || || || || (_____    | |   | (__    | (____)|
    |  ___  ||  ___  || |(_)| |(_____  )   | |   |  __)   |     __)
    | (   ) || (   ) || |   | |      ) |   | |   | (      | (\ (   
    | )   ( || )   ( || )   ( |/\____) |   | |   | (____/\| ) \ \__
    |/     \||/     \||/     \|\_______)   )_(   (_______/|/   \__/
                                                                   
     _        _______  _______  ______   _______ _________   ______   _______ _________
    | \    /\(  ___  )(       )(  ___ \ (  ___  )\__   __/  (  ___ \ (  ___  )\__   __/
    |  \  / /| (   ) || () () || (   ) )| (   ) |   ) (     | (   ) )| (   ) |   ) (   
    |  (_/ / | |   | || || || || (__/ / | (___) |   | |     | (__/ / | |   | |   | |   
    |   _ (  | |   | || |(_)| ||  __ (  |  ___  |   | |     |  __ (  | |   | |   | |   
    |  ( \ \ | |   | || |   | || (  \ \ | (   ) |   | |     | (  \ \ | |   | |   | |   
    |  /  \ \| (___) || )   ( || )___) )| )   ( |   | |     | )___) )| (___) |   | |   
    |_/    \/(_______)|/     \||/ \___/ |/     \|   )_(     |/ \___/ (_______)   )_( """)
    print(f"""
    Your balance: {balance}""")
    print(f"""
    Select command:
    1) Auto-upgrade {tupgrade};
    2) Auto-tap {ttap}
    3) Write code
    4) Start farm""")
    command = input_command()
    match command:
        case '1':
            aupgrade = not aupgrade
            start(aupgrade, atap)
        case '2':
            atap = not atap
            start(aupgrade, atap)
        case '3':
            code = input('Write cipher: ')
            code_write(code)
            print('Bonus claimed')
            time.sleep(2)
            start()
        case '4':
            print('Starting AUTO')
            time.sleep(5)
            while True:
                auto_upgrade()
                auto_tap()
                auto_sync()
                print('Waiting 60 sec')
                time.sleep(60)
        case _:
            print("Wrong command.")
            time.sleep(2)
            start()

