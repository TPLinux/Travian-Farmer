# By: https://twitter.com/@i127001
# coding: utf8
from time import sleep
import sys
print("\n\n-----------------")
print("Travian Farmer v1.0 - Arabian Coder By: @i127001")
print("Vists me at Twitter: https://twitter.com/i127001")
print("-----------------\n\n")

loop = ''
while(loop != 'e'):
    print('\n------\n')
    print("Insert Your Option:\n")
    print("[0]-> Search Farms")
    print("[1]-> Raid Farms")
    print("[e]-> Exit")
    print("")
    user_option = raw_input("[option]-> ")
    if(user_option == '0'):
        import searcher  # noqa
    elif(user_option == '1'):
        import raider  # noqa
    elif(user_option == 'e'):
        print("Exiting...")
        sleep(2)
        print('-------')
        print("Farmer Stopped!")
        print('-------')
        sys.exit()
    else:
        pass
