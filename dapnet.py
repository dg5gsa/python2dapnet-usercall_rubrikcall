# Basierend auf senden.py von DF7FL (Phillip)   https://github.com/DL7FL
# weiterentwickelt von DG5GSA (Stefan)          https://github.com/dg5gsa
# Version 1.0 - Stand 13.05.2018

# In dieser Datei sind keine Anpassungen erforderlich !!!


#Import der benötigten Module

import requests
from requests.auth import HTTPBasicAuth
import json
import pprint


#   Definition der PUT Funktion (Rubrik Call senden)

def PUT(text, rubricName, number, login, passwd, url):
    json_string =json.dumps({"text": text, "rubricName": rubricName, "number": number })
    pprint.pprint(json_string)
    response = requests.post(url, data=json_string, auth=HTTPBasicAuth(login, passwd))
    return response.status_code



#   Definition der send Funktion (User Call senden)

def send(text, callsign, login, passwd, url, txgroup="dl-all"):
    json_string =json.dumps({"text": text, "callSignNames": callsign, "transmitterGroupNames": [txgroup], "emergency": False})
    pprint.pprint(json_string)
    response = requests.post(url, data=json_string, auth=HTTPBasicAuth(login, passwd))
    return response.status_code

def single_callsign(callsign_list):
    for callsign in callsign_list:
        send(text, callsign, login, passwd, url)
        return




