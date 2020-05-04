# MIT License
#
# Copyright (c) 2020 Skuzzy xD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pyfiglet
from get_proxyscrape import *

welcome = pyfiglet.figlet_format("ProxyGrab", font = "slant")
welcome += "\t\t\t\tBy: Skuzzy xD\n\n"
#Start Message
print(welcome)

#Menu for Choosing Proxy Type
menu_proxy = input("*Proxies are grabbed from Proxyscrape at the moment*\n\nChoose an option:\n1. Http/Https\n2. Socks4\n3. Socks4a\n4. Socks5\n5. All Proxies\n\nEnter your choice: ")

#Choosing Proxy Type
if menu_proxy in ["1","http","https"]:
    ptype = "http"
    get_proxyscrape(ptype)

elif menu_proxy in ["2","socks4"]:
    ptype = "socks4"
    get_proxyscrape(ptype)

elif menu_proxy in ["3","socks4a"]:
    ptype = "socks4a"
    get_proxyscrape(ptype)

elif menu_proxy in ["4","socks5"]:
    ptype = "socks5"
    get_proxyscrape(ptype)

elif menu_proxy in ["5", "all"]:
    ptype = ("http", "socks4", "socks4a", "socks5")
    for i in ptype: #Iterating through all items in tuple
        get_proxyscrape(i)


#If no option selected from above, return error
else:
    incorrectopt = input("You have chosen an incorrect option!\nPress Enter/Return key to exit")
