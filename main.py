import time, requests, config

# Read user_agent.txt with good format so session.headers.update doesn't crap itself
with open("user_agent.txt", "r", encoding="utf-8") as user_file:
    user_agent = user_file.read()

session = requests.Session()
session.headers.update(user_agent)


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
        time.sleep(0.25)
        deep_info = requests.get(deep_api_request)
        print(deep_info.json())

def check_connection_status():
    server_pug_rest = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/property/MolecularFormula/JSON"
    server_status = requests.get(server_pug_rest)
    print(server_status.status_code, server_status.headers.get("X-Throttling-Control"))

# MAIN APP*
compound_name = input("Please enter the name of the compound you want to search: ")
check_connection_status()
time.sleep(0.5)
cid = get_cid_by_name(compound_name)
time.sleep(0.5)
search_basic_info(compound_name)
time.sleep(0.5)
search_deep_info(cid)
