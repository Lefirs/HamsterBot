from imports import *
from func_autoupgrade import auto_upgrade

def input_command():
    command = input("Write command num: ")
    return command

def start():
    os.system('cls')
    os.system("title HamsterKombat Bot")
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
    print("""
    Select command:
    1) Auto-upgrade;
    2) Auto-tap""")
    command = input_command()
    match command:
        case '1':
            auto_upgrade()
            start()
        case '2':
            print('Not work command')
            start()
        case _:
            print("Wrong command.")
            time.sleep(2)
            start()
