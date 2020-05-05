import os
import time
import sites

#For figlet font
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
init(strip=not sys.stdout.isatty()) #For coloured text

#Function defining to get proxies of type told
def getproxies(ptype):
    sites.proxyscrape(ptype)
    sites.proxylist(ptype)

time.sleep(2) #2 second wait

#Make a directory to store proxies
try:
    os.mkdir("Proxies")
except FileExistsError:
    pass

welcome = figlet_format("ProxyGrab v1.2", font = "slant")
welcome += "\t\t\t\tBy: Skuzzy xD\n\n"

#Start Message
cprint(welcome, "green")

time.sleep(3) #2 second wait

#Menu for Choosing Proxy Type
cprint("Proxies are grabbed from:", "red")
cprint("*proxyscrape.com*\n*proxy-list.download*\n\n", "yellow")
cprint("Choose an option:", "red")
cprint("1. Http/Https\n2. Socks4\n3. Socks5\n4. All Proxies\n5. Exit/Cancel", "cyan")
menu_proxy = input("\nEnter your choice: ").lower()

#Choosing Proxy Type
if menu_proxy in ["1","http","https"]:
    ptype = "http"
    time.sleep(2) #2 second wait given to prevent API Overload
    getproxies(ptype)

elif menu_proxy in ["2","socks4"]:
    ptype = "socks4"
    time.sleep(2) #2 second wait given to prevent API Overload
    getproxies(ptype)

elif menu_proxy in ["3","socks5"]:
    ptype = "socks5"
    time.sleep(2) #2 second wait given to prevent API Overload
    getproxies(ptype)

elif menu_proxy in ["4", "all"]:
    ptype = ("http", "socks4", "socks5")
    for i in ptype: #Iterating through all items in tuple
        time.sleep(2) #2 second wait given to prevent API Overload
        getproxies(i)

elif menu_proxy in ["5", "exit", "cancel"]:
    time.sleep(1)
    print("Exiting Program...")
    time.sleep(2)
    sys.exit()

#If no option selected from above, return error
else:
    incorrectopt = input("You have chosen an incorrect option!\nPress Enter/Return key to exit")
