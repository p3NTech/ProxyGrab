import os
import time
import sites
from update import *

#For figlet font
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
init(strip=not sys.stdout.isatty()) #For coloured text

#Check if using latest version or not
check_update()

#Function defining to get proxies of type told
def getproxies(ptype):
    sites.proxyscrape(ptype)
    sites.proxylist(ptype)

time.sleep(2) #2 second wait

f=open("CURRENTVERSION", "r")
contents =f.read()
cv = contents.replace("\n","")

wlcm_text = "ProxyGrab v" + cv

welcome = figlet_format(wlcm_text, font = "slant")
welcome += "\t\t\t\tBy: Skuzzy xD\n\n"

#Start Message
cprint(welcome, "green")

#Make a directory to store proxies
try:
    os.mkdir("Proxies")
except FileExistsError:
    pass

time.sleep(3) #3 second wait

#Menu for Choosing Proxy Type
cprint("Proxies are grabbed from:", "red")
cprint("*proxyscrape.com*\n*proxy-list.download*", "yellow")
cprint("\n\nChoose an option:", "red")
cprint("1. HTTP\n2. HTTPS\n3. Socks4\n4. Socks5\n5. All Proxies\n6. Exit/Cancel", "cyan")
menu_proxy = input("\nEnter your choice: ").lower()

#Choosing Proxy Type
if menu_proxy in ("1", "https"):
    ptype = "http"
    time.sleep(2) #2 second wait given to prevent API Overload
    getproxies(ptype)

if menu_proxy in ("2", "https"):
    ptype = "https"
    time.sleep(2) #2 second wait given to prevent API Overload
    getproxies(ptype)

elif menu_proxy in ("3", "socks4"):
    ptype = "socks4"
    time.sleep(2) #2 second wait given to prevent API Overload
    getproxies(ptype)

elif menu_proxy in ("4", "socks5"):
    ptype = "socks5"
    time.sleep(2) #2 second wait given to prevent API Overload
    getproxies(ptype)

elif menu_proxy in ("5", "all"):
    ptype = ("http", "https", "socks4", "socks5")
    for i in ptype: #Iterating through all items in tuple
        time.sleep(2) #2 second wait given to prevent API Overload
        getproxies(i)

elif menu_proxy in ("6", "exit", "cancel"):
    print("Exiting Program...")
    time.sleep(1)
    sys.exit()

#If no option selected from above, return error
else:
    incorrectopt = input("You have chosen an incorrect option!\nPress Enter/Return key to exit")
