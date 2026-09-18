import requests # necesario para las API requests

# 1. Definimos la dirección exacta de lo que queremos buscar
url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/property/MolecularFormula,MolecularWeight/JSON"

# 2. El "mensajero" va a esa dirección y trae la respuesta
respuesta = requests.get(url)

# 3. Convertimos esa respuesta de texto a un diccionario de Python
datos = respuesta.json()

# 4. Mostramos todo el paquete en la terminal
print(datos)
