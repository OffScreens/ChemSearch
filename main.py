import time
import requests
import config

def search_basic_info(compound_name): # Outputs basic PUG information
    api_request = config.get_compound_base_info(compound_name)
    data = requests.get(api_request)
    print(data.json())

def get_cid_by_name(compound_name): # Gets the compound CID identifier by its name (necessary for search_deep_info)
    cid_url = config.get_cid_url(compound_name)
    cid = requests.get(cid_url)

    if cid.status_code == 200: # If PubChem gives a positive response
        cid_number = cid.json()
        print("Compound identified")
        return cid_number["IdentifierList"]["CID"][0] # Grab the CID number
    else:
        print(f"No such compound by the name {compound_name}")

def search_deep_info(cid):
    for header in config.PUG_VIEW_HEADERS:
        deep_api_request = config.get_specific_info(cid, header)
        time.sleep(0.2)
        deep_info = requests.get(deep_api_request)
        print(deep_info.json())

compound_name = input("Please enter the name of the compound you want to search: ")
cid = get_cid_by_name(compound_name)
search_basic_info(compound_name)
search_deep_info(cid)
