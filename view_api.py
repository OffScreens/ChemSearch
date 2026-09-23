import config
import requests
import time

# Repeat User Agent, because I can't figure out how to use the one in main.py :)
with open("user_agent.txt", "r", encoding="utf-8") as user_file:
    user_agent = user_file.read().rstrip()
print("The user agent is: "+user_agent)

session = requests.Session()
session.headers["User-Agent"] = user_agent

def ghs_info(cid):
    view_url = config.get_specific_info(cid, "GHS+Classification")
    ghs_request = session.get(view_url)
    time.sleep(0.75)
    return ghs_request.json()

def toxic_info(cid):
    view_url = config.get_specific_info(cid, "Toxicological+Information")
    toxic_request = session.get(view_url)
    time.sleep(0.75)
    return toxic_request.json()

def corrosion_info(cid):
    view_url = config.get_specific_info(cid, "Skin+Corrosion%2FIrritation")
    corrosion_request = session.get(view_url)
    time.sleep(0.75)
    return corrosion_request.json()

def reactivity_info(cid):
    view_url = config.get_specific_info(cid, "Reactivity+Profile")
    reactivity_request = session.get(view_url)
    time.sleep(0.75)
    return reactivity_request.json()

def storage_info(cid):
    view_url = config.get_specific_info(cid, "Storage+Conditions")
    storage_request = session.get(view_url)
    time.sleep(0.75)
    return storage_request.json()

def ppe_info(cid):
    view_url = config.get_specific_info(cid, "Personal+Protective+Equipment+(PPE)")
    ppe_request = session.get(view_url)
    time.sleep(0.75)
    return ppe_request.json()
