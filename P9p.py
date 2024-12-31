from itertools import count
import os


print (''' 
░▒▓███████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░       ░▒▓██████▓▒░                                                                                                                                              
    ''')
host = input('IP: ')

counter = 0

goal = 987654321369

while counter <= goal:
    print("---------------------------------------")
    send_ping = os.system("ping " + host)
    counter += 1
    print(send_ping)


