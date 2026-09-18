import requests # necesario para las API requests

# Dirección de lo que queremos buscar
url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/property/MolecularFormula,MolecularWeight/JSON"

# Buscamos la respuesta de la búsqueda
respuesta = requests.get(url)

# Convertimos esa respuesta de texto a un diccionario de Python
datos = respuesta.json()
print(datos)
