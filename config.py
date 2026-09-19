
# Returns; MolecularWeight, IUPACName and CID number
PUBCHEM_PUG = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

def get_compound_name(compound_name):
    return f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound_name}/property/IUPACName,MolecularWeight/JSON"

# Returns;
PUBCHEM_PUG_VIEW = "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view"
