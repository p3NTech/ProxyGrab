import requests
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
init(strip=not sys.stdout.isatty()) #For coloured text

update_url = "https://raw.githubusercontent.com/SkuzzyxD/ProxyGrab/master/CURRENTVERSION"
repo_url = "https://github.com/SkuzzyxD/ProxyGrab"
update_string = "You're using an old version of the app, please update the app from below link"

f=open("CURRENTVERSION", "r")
contents =f.read()
cv = contents.replace("\n","")
current_version = float(cv)

def check_update():
    response = requests.get(update_url)
    if response.status_code == 200:
        response = response.text
        rv = response.replace("\n","")
        remote_version = float(rv)
        if remote_version > current_version:
            cprint(update_string, "red")
            cprint(repo_url, "cyan")
            cprint("\n*Exiting now, update to latest version to use again*\n", "yellow")
            f.close()
            sys.exit()
        if remote_version == current_version:
            f.close()
            pass
        if remote_version < current_version:
            cprint("Don't change CURRENTVERSION file, you might have problems in program.", "yellow")
