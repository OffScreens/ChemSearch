import config
import view_api
import requests
import time
import info_parsing

# USER AGENT FOR API REQUESTS
with open("user_agent.txt", "r", encoding="utf-8") as user_file:
    user_agent = user_file.read().rstrip()

session = requests.Session()
session.headers["User-Agent"] = user_agent

def search_basic_info(compound_name): # Outputs basic PUG information
    api_request = config.get_compound_base_info(compound_name)
    basic_data = session.get(api_request)
    return basic_data.json()

def check_connection_status():
    server_pug_rest = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/property/MolecularFormula/JSON"
    server_status = session.get(server_pug_rest)
    print(server_status.status_code, server_status.headers.get("X-Throttling-Control"))

# Display Connection Status
check_connection_status()
time.sleep(1)

# Extract all the info and display it in a friendly manner
compound_found = False
while not compound_found:
    compound_name = input("Please enter the name of the compound you want to search: ")
    basic_data = search_basic_info(compound_name) # REQUEST DATA FROM PUBCHEM

    if "PropertyTable" in basic_data:
        # ---------- CID NUMBER
        cid_number = basic_data["PropertyTable"]["Properties"][0]["CID"]
        print(f"  CID identification number: {cid_number}")
        # ---------- IUPAC NAME
        iupac_name = basic_data["PropertyTable"]["Properties"][0]["IUPACName"]
        print(f"  IUPAC Name: {iupac_name}")
        # ---------- MOLECULAR WEIGHT
        molecular_weight = basic_data["PropertyTable"]["Properties"][0]["MolecularWeight"]
        print(f"  Molecular weight: {molecular_weight}")

        # PUG VIEW info
        print("-- GHS HAZARD STATEMENTS --")
        ghs_info = view_api.ghs_info(cid_number)
        info_parsing.ghs_parsing(ghs_info)

        print("-- TOXICITY SUMMARY --")
        toxic_info = view_api.toxic_info(cid_number)
        info_parsing.toxicology_parsing(toxic_info)

        print("-- HANDLING & STORAGE CONDITIONS --")
        storage_info = view_api.storage_info(cid_number)
        info_parsing.storage_conditions(storage_info)
        break
    else:
        print("Compound not found")

#corrosion_info = view_api.corrosion_info(cid_number)
#reactivity_info = view_api.reactivity_info(cid_number)
#storage_info = view_api.storage_info(cid_number)
#ppe_info = view_api.ppe_info(cid_number)
