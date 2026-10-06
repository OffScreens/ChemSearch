import json
from pathlib import Path

# This is just for testing purposes, change for definitive with ghs_data or json.
json_path = Path("testing/sample_data/handling_storage_aspirin.json")
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

def ghs_parsing(ghs_info):
    record = ghs_info.get("Record", {}) # Dictionary, we use .get
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
                                        print(f"   - {text}")
    return ["GHS hazard statements not found."]
    # Notice that there isn't any variable storing GHS statements, maybe for later.

def toxicology_parsing(toxic_info):
    record = toxic_info.get("Record", {})
    sections = record.get("Section", [])
    for section in sections:
        if section.get("TOCHeading") == "Toxicity":
            toxicity = section.get("Section", [])
            for toxic_infor in toxicity:
                if toxic_infor.get("TOCHeading") == "Toxicological Information":
                    subsection = toxic_infor.get("Section", [])
                    for info in subsection:
                        if info.get("TOCHeading") == "Toxicity Summary":
                            toxic_sum = info.get("Information",  [])
                            for value in toxic_sum:
                                values = value.get("Value", {})
                                markup_list = values.get("StringWithMarkup", [])
                                for sum in markup_list:
                                    summary = sum.get("String")
                                    print(f"   - {summary}")

    return ["Toxicology information not found."]

def storage_conditions(storage_info):
    record = storage_info.get("Record", {})
    sections = record.get("Section", [])
    for section in sections:
        if section.get("TOCHeading") == "Safety and Hazards":
            subsections = section.get("Section", [])
            for subsection in subsections:
                if subsection.get("TOCHeading") == "Handling and Storage":
                    information = subsection.get("Section", [])
                    for infos in information:
                        if infos.get("TOCHeading") == "Nonfire Spill Response":
                            spill_resp = infos.get("Information", [])
                            for value in spill_resp:
                                values = value.get("Value", {})
                                markup_list = values.get("StringWithMarkup", [])
                                for condition in markup_list:
                                    conditions = condition.get("String")
                                    print(f"   - {conditions}")

    return ["Storage conditions & handling information not found"]
