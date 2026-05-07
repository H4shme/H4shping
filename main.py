import os

def clear():
    if os.name == 'nt':
        os.system("cls")
    else: 
        os.system("clear")
try:
    import socket
    from colorama import Fore 
    import time
    import requests
    import json

except ImportError:
    clear()
    print("Please install requirements with : \npip3 install -r requirements.txt ")
    pip = input("Would you like me to install it for you ? y/n\n > ").lower()
    if pip == "y":
        os.system("pip3 install -r requirements.txt")
        clear()
        print("Modules installed please restart with python3 main.py")
        exit()
    else:
        exit()


banner = """
                              $$$$$                                          
                              $:::$                                          
HHHHHHHHH     HHHHHHHHH   $$$$$:::$$$$$$                 hhhhhhh             
H:::::::H     H:::::::H $$::::::::::::::$                h:::::h             
H:::::::H     H:::::::H$:::::$$$$$$$::::$                h:::::h             
HH::::::H     H::::::HH$::::$       $$$$$                h:::::h             
  H:::::H     H:::::H  $::::$                ssssssssss   h::::h hhhhh       
  H:::::H     H:::::H  $::::$              ss::::::::::s  h::::hh:::::hhh    
  H::::::HHHHH::::::H  $:::::$$$$$$$$$   ss:::::::::::::s h::::::::::::::hh  
  H:::::::::::::::::H   $$::::::::::::$$ s::::::ssss:::::sh:::::::hhh::::::h 
  H:::::::::::::::::H     $$$$$$$$$:::::$ s:::::s  ssssss h::::::h   h::::::h
  H::::::HHHHH::::::H              $::::$   s::::::s      h:::::h     h:::::h
  H:::::H     H:::::H              $::::$      s::::::s   h:::::h     h:::::h
  H:::::H     H:::::H  $$$$$       $::::$ssssss   s:::::s h:::::h     h:::::h
HH::::::H     H::::::HH$::::$$$$$$$:::::$s:::::ssss::::::sh:::::h     h:::::h
H:::::::H     H:::::::H$::::::::::::::$$ s::::::::::::::s h:::::h     h:::::h
H:::::::H     H:::::::H $$$$$$:::$$$$$    s:::::::::::ss  h:::::h     h:::::h
HHHHHHHHH     HHHHHHHHH      $:::$         sssssssssss    hhhhhhh     hhhhhhh
                             $$$$$                                           
                                                                                             
                            PORT SCANNER BY H4$H                             """

opened_port = []



with open('lib/top_100_common_ports.json') as f:
    data = json.load(f)



def check_port(ip, start_port, end_port):
    oneportatleast = False

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            opened_port.append(ip+ ":" + str(port))
            print(Fore.GREEN + ip + ":" + str(port) + " (OPEN)")
            oneportatleast = True
        else:
            print("\r"+Fore.RED+ip+":" + str(port) + " (CLOSED)")
            


    if oneportatleast == True:
        clear()
        print(Fore.GREEN+banner)
        print(f"Opened ports = ", *opened_port)
    else:
        clear()
        print(Fore.RED+banner)
        print("No port founded :/")


def check_port_range():
    print(Fore.WHITE+banner)
    ip = input(Fore.BLUE + "IP : ")
    start_port = int(input(Fore.RED + "Start Port : "))
    end_port = int(input(Fore.RED + "End Port : "))
    clear()
    print(Fore.BLUE+banner)
    check_port(ip, start_port, end_port)




def top100commonsports(ip):
    for entry in data:
        top100proto = str(entry["proto"])
        top100port = int(entry["port"])
        top100service = str(entry['service'])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, int(top100port)))
        if result == 0:
            print(Fore.GREEN + str(top100port) + " | " + top100service + " (" + top100proto +")")
            opened_port.append(str(top100port) + " | " + top100service + " (" + top100proto +")")
            oneportatleast = True
        else: 
            print("\r"+Fore.RED+str(top100port)+" | " + top100service + " (" + top100proto + ")")

    if oneportatleast == True:
        clear()
        print(Fore.GREEN+banner)
        print(Fore.WHITE+"Opened ports = ", *opened_port)
    else:
        clear()
        print(Fore.RED+banner)
        print("No port founded :/")

def save_scans():
    pass


def main():
    clear()
    print(Fore.WHITE+banner + "\n\n")
    print(Fore.WHITE+"Choose a scan type\n\n1-Scan by port range\n2-Scan the most 100 common ports\n\n")
    menu_choice = input(Fore.WHITE+"> ")
    if menu_choice == "1":
        clear()
        check_port_range()
    elif menu_choice == "2":
        clear()
        print(Fore.WHITE+banner)
        ip = input(Fore.BLUE+"IP : ")
        top100commonsports(ip)
    else:
        print(Fore.RED+"Syntax Error")
        time.sleep(1)
        main()

#Check if it's launched itself and not as an module
if __name__ == '__main__':
    main()

