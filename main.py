import config
import requests
import time

# Read user_agent.txt with good format so session.headers doesn't crap itself
with open("user_agent.txt", "r", encoding="utf-8") as user_file:
    user_agent = user_file.read().rstrip()
print("The user agent is: "+user_agent)

# Make all session.get have the user agent header, having this here prevents
# having to write it every request.
session = requests.Session()
session.headers["User-Agent"] = user_agent

def search_basic_info(compound_name): # Outputs basic PUG information
    api_request = config.get_compound_base_info(compound_name)
    basic_data = session.get(api_request)
    return basic_data.json()

def search_deep_info(cid):
    for header in config.PUG_VIEW_HEADERS:
        deep_api_request = config.get_specific_info(cid, header)
        time.sleep(0.75)
        deep_info = session.get(deep_api_request)
        return deep_info.json()



def check_connection_status():
    server_pug_rest = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/property/MolecularFormula/JSON"
    server_status = session.get(server_pug_rest)
    print(server_status.status_code, server_status.headers.get("X-Throttling-Control"))

# MAIN APP*
compound_name = input("Please enter the name of the compound you want to search: ")

# Connection status
check_connection_status()
time.sleep(1)

# Extract all the info and display it in a friendly manner
basic_data = search_basic_info(compound_name) # REQUEST DATA FROM PUBCHEM
# ---------- CID NUMBER
cid_number = basic_data["PropertyTable"]["Properties"][0]["CID"]
print(f"  CID identification number: {cid_number}")
# ---------- IUPAC NAME
iupac_name = basic_data["PropertyTable"]["Properties"][0]["IUPACName"]
print(f"  IUPAC Name: {iupac_name}")
# ---------- MOLECULAR WEIGHT
molecular_weight = basic_data["PropertyTable"]["Properties"][0]["MolecularWeight"]
print(f"  Molecular weight: {molecular_weight}")

deep_info = search_deep_info(cid_number)


time.sleep(1)
search_deep_info(cid_number)
