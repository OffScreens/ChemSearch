#import main
import json
from pathlib import Path

# This is just for testing purposes, change for definitive with ghs_data or json.
json_path = Path("sample_data/GHSaspirin.json")
with open(json_path, "r", encoding="utf-8") as f:
    datos = json.load(f)

#print(datos)

def ghs_parsing(datos):
#    record = main.ghs_info.get("Record", {})
    record = datos.get("Record", {}) # Dictionary, we use .get
    sections = record.get("Section", []) # List, use for loop
    for section in sections:
        if section.get("TOCHeading") == "Safety and Hazards":
            hazards_sections = section.get("Section", [])
            for hazard_section in hazards_sections:
                if hazard_section.get("TOCHeading") == "Hazards Identification":
                    ghs_sections = hazard_section.get("Section", [])
                    for ghs_section in ghs_sections:
                        if ghs_section.get("TOCHeading") == "GHS Classification":
                            information = ghs_section.get("Information", [])
                            for info in information:
                                if info.get("Name") == "GHS Hazard Statements":
                                    values = info.get("Value", {})
                                    markup_list = values.get("StringWithMarkup", [])
                                    # Now inside of "GHS Hazard Statements", search
                                    # recursively for all statements
                                    for statement in markup_list:
                                        text = statement.get("String")
                                        print(f"- {text}")





    return []
    # Notice that there isn't any variable storing GHS statements, maybe for later.

ghs_parsing(datos)





# Lots of work to be done
