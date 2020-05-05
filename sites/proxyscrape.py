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

from os import path #To delete old files
import requests #To request data using Api

#Function to get proxies from Proxyscrape
def proxyscrape(ptype):

    #Api URL, the trailing / is necessary to complete the request in correct way...
    api_url = "https://api.proxyscrape.com/"

    #Two Requests, one to get proxies and other to get amount of proxies
    proxyscrape_ptype_url = f"{api_url}?request=displayproxies&proxytype={ptype}" #Get Proxies
    proxyscrape_amtproxies_url = f"{api_url}?request=amountproxies&proxytype={ptype}" #Get number of proxies

    #Get both responses from Server
    proxyscrape_ptype_response = requests.get(proxyscrape_ptype_url)
    proxyscrape_amtproxies_response = requests.get(proxyscrape_amtproxies_url)

    #If both responses are true, then proceed, else display error
    if proxyscrape_ptype_response.status_code == 200 and proxyscrape_amtproxies_response.status_code == 200:
        filename = str(f"{ptype}_proxyscrape_proxygrab.txt") #filename as string
        file = open(filename, "w") #OPen the file in write mde, denoted by "w" parameter

        #Get text from response
        proxyscrape_proxies = proxyscrape_ptype_response.text #Get Proxies
        proxyscrape_amt_proxies = proxyscrape_amtproxies_response.text #Get amount of proxies

        file.write(proxyscrape_proxies) #save proxies to a file
        file.close() #close the file
        print(f"Saved {proxyscrape_amt_proxies} {ptype} proxies to: {filename}")

    #If status is not equal to 200
    else:
        error = input("An error occured!\nResponse not equal  200")
