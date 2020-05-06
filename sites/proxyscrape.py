import requests #To request data using Api

#Function to get proxies from Proxyscrape
def proxyscrape(ptype):

    #Api URL, the trailing / is necessary to complete the request in correct way...
    api_url = "https://api.proxyscrape.com/"

    #Two Requests, one to get proxies and other to get amount of proxies
    proxyscrape_ptype_url = f"{api_url}?request=displayproxies&proxytype={ptype}" #Get Proxies

    #Get both responses from Server
    proxyscrape_ptype_response = requests.get(proxyscrape_ptype_url)

    #If both responses are true, then proceed, else display error
    if proxyscrape_ptype_response.status_code == 200:
        filename = str(f"Proxies/{ptype}_proxyscrape_proxygrab.txt") #filename as string
        file = open(filename, "w") #OPen the file in write mde, denoted by "w" parameter

        #Get text from response
        proxyscrape_proxies = proxyscrape_ptype_response.text #Get Proxies

        file.write(proxyscrape_proxies) #save proxies to a file
        file.close() #close the file
        print(f"Saved {ptype} proxies to: {filename}")

    #If status is not equal to 200
    else:
        print("An error occured!\nResponse not equal  200")
        pass
