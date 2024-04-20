import json
from time import sleep
import threading
from datetime import datetime
import os
try:
    import ctypes
    import tls_client
    from pystyle import Write, Colors
    from colorama import Fore, init
    import colorama
except:
    os.system('pip install ctypes')
    os.system('pip install tls_client')
    os.system('pip install pystyle')
    os.system('pip install colorama')


print_lock = threading.Lock()

init(convert=True)
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pink = Fore.MAGENTA
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET

checked = 0
valid = 0

file_path = "list.txt"

def delete_first_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        file.writelines(lines[1:])

def time_rn():
    current_datetime = datetime.now()
    current_hour = current_datetime.hour
    current_minute = current_datetime.minute 
    return ("{:02d}:{:02d}".format(current_hour, current_minute))

def gay():
    global checked, valid
    ctypes.windll.kernel32.SetConsoleTitleW(f'.gg/lord • [C: {checked} | V: {valid}]')

    session = tls_client.Session(
    client_identifier="chrome123",
    random_tls_extension_order=True)

    with print_lock:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if not lines:
                print(Fore.MAGENTA + f"[!] Waiting for usernames in {file_path}...")
                sleep(5)
                return
            
            user = lines[0].strip()
            try:
                response = session.get(f"https://api.mojang.com/users/profiles/minecraft/{user}")
                data = response.json()

                try:
                    profile_name = data.get("name")
                    id = data.get('id')

                    if id == None:
                        try:
                            err = data.get('errorMessage')
                            
                            if err != f"Couldn't find any profile with name {user}":
                                print(f"{pink}[{reset}{time_rn()}{pink}] {yellow}RATE{reset} Rate Limited ", end="")
                                Write.Print(f"[{user}]" + "\n", Colors.red_to_yellow, interval=0.000)

                            elif err == f"Couldn't find any profile with name {user}":
                                with open("available.txt", "a") as f:
                                    f.write(f"{user}\n")

                                    print(f"{pink}[{reset}{time_rn()}{pink}] {blue}NAME{reset} Available ", end="")
                                    Write.Print(f"[{user}]" + "\n", Colors.green_to_white, interval=0.000)
                                    delete_first_line(file_path)

                                    checked += 1
                                    valid += 1

                        except Exception as e:
                            print(e)

                    elif id != None:
                        print(f"{pink}[{reset}{time_rn()}{pink}] {blue}NAME{reset} Taken User ", end="")
                        Write.Print(f"[{user}]" + "\n", Colors.red_to_white, interval=0.000)
                        delete_first_line(file_path)

                        checked += 1

                except Exception as e:
                    pass
            except Exception as e:
                pass

Write.Print(f"""
        ▄▄▌        ▄▄▄  ·▄▄▄▄  
        ██•  ▪     ▀▄ █·██▪ ██ 
        ██▪   ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌
        ▐█▌▐▌▐█▌.▐▌▐█•█▌██. ██ 
        .▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•
                                                                              
""", Colors.blue_to_purple, interval=0.000)
sleep(0.5)

threads = []

while True:
    for i in range(int(2)):
        thread = threading.Thread(target=gay, name=f"LordTheBest")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
