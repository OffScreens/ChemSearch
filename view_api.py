import time

import requests

import config

# Repeat User Agent, because I can't figure out how to use the one in main.py :)
with open("user_agent.txt", "r", encoding="utf-8") as user_file:
    user_agent = user_file.read().rstrip()

session = requests.Session()
session.headers["User-Agent"] = user_agent

def ghs_info(cid_number):
    view_url = config.get_specific_info(cid_number, "GHS+Classification")
    ghs_request = session.get(view_url)
    time.sleep(0.75)
    return ghs_request.json()

def toxic_info(cid_number):
    view_url = config.get_specific_info(cid_number, "Toxicological+Information")
    toxic_request = session.get(view_url)
    time.sleep(0.75)
    return toxic_request.json()

def corrosion_info(cid_number):
    view_url = config.get_specific_info(cid_number, "Skin+Corrosion%2FIrritation")
    corrosion_request = session.get(view_url)
    time.sleep(0.75)
    return corrosion_request.json()

def reactivity_info(cid_number):
    view_url = config.get_specific_info(cid_number, "Reactivity+Profile")
    reactivity_request = session.get(view_url)
    time.sleep(0.75)
    return reactivity_request.json()

def storage_info(cid_number):
    view_url = config.get_specific_info(cid_number, "Storage+Conditions")
    storage_request = session.get(view_url)
    time.sleep(0.75)
    return storage_request.json()

def ppe_info(cid_number):
    view_url = config.get_specific_info(cid_number, "Personal+Protective+Equipment+(PPE)")
    ppe_request = session.get(view_url)
    time.sleep(0.75)
    return ppe_request.json()
