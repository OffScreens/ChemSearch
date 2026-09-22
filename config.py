
# Returns; MolecularWeight, IUPACName and CID number
PUBCHEM_PUG = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"

def get_compound_base_info(compound_name):
    return f"{PUBCHEM_PUG}compound/name/{compound_name}/property/IUPACName,MolecularWeight,MolecularFormula/JSON"

# Returns;
PUBCHEM_PUG_VIEW = "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound"

# For the sake of not repeating code, we create a "dynamic" link
PUG_VIEW_HEADERS = [
    "GHS+Classification",
#    "Toxicological+Information",
#    "Skin+Corrosion%2FIrritation",
#    "Reactivity+Profile",
#    "Storage+Conditions",
#    "Personal+Protective+Equipment+(PPE)",
]
# For PUG_VIEW API we need the CID, cannot use name, so a function is created to convert name to CID
# Complemented by function get_cid_by_name in main.py
def get_cid_url(compound_name):
    return f"{PUBCHEM_PUG}/compound/name/{compound_name}/cids/JSON"

def get_specific_info(cid, header):
    return f"{PUBCHEM_PUG_VIEW}/{cid}/JSON?heading={header}"
