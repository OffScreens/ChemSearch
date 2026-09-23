
# Returns; MolecularWeight, IUPACName and CID number
PUBCHEM_PUG = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"

def get_compound_base_info(compound_name):
    return f"{PUBCHEM_PUG}compound/name/{compound_name}/property/IUPACName,MolecularWeight,MolecularFormula/JSON"

# Returns;
PUBCHEM_PUG_VIEW = "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound"

# For PUG_VIEW API we need the CID
def get_cid_url(compound_name):
    return f"{PUBCHEM_PUG}/compound/name/{compound_name}/cids/JSON"

def get_specific_info(cid, header):
    return f"{PUBCHEM_PUG_VIEW}/{cid}/JSON?heading={header}"
