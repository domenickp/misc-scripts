#!venv/bin/python

import sys
import requests

noip_url = "https://dynupdate.no-ip.com/nic/update"
getip_url = "http://icanhazip.com/"
# echo username:password | base64
logon_session_creds = "ouputfromabovecommandgoeshere"

def get_myip():
    r = requests.get(getip_url)
    r.encoding = 'utf-8'
    return r.text

def update_ddns(myip):
    headers = {'Authorization': 'Basic ' + logon_session_creds,
               'Host': 'myhost.ddns.net',
               'User-Agent': 'Doms Pro-fessional Python Client/0.01 domenick.petrella@gmail.com'}
    r = requests.get(noip_url, headers=headers)
    return r.text

def do_update():
    myip = get_myip()
    retval = update_ddns(myip)
    print(retval)

if __name__ == "__main__":
    do_update()
