#information gathering tool Project -01

import sys
import requests
import socket
import json

if len(sys.argv[1]) < 2:
    print("Usage: sys.exit(1) + sys.argv[0] + <url>")

req = requests.get("https://"+sys.argv[1])
print("\n"+str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+gethostby_+"\n")

req_two = requests.get("https://ipinfo.io/"+gethostby_ +"/json")

resp_ = json.loads(req_two.text)
print("internal hostname: "+resp_ ['hostname'])
print("Geographical Location: "+resp_ ['loc'])
print("City: "+resp_['city'])
print("Region "+resp_['region'])
print("Country: "+resp_['country'])
print("Post Code: "+resp_['postal'])
print("Owner Organisation: "+resp_ ['org'])
print("Timezone : " + resp_['timezone'])

