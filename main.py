import requests # necesario para las API requests
import config

def search_compound(compund_name):
    api_request = config.get_compound_name(compound_name)
    data = requests.get(api_request)
    print(data.json())

compound_name = input("Please enter the name of the compound you want to search: ")
search_compound(compound_name)
