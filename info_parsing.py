import main
import json
from pathlib import Path

# This is just for testing purposes, change for definitive with ghs_data or json.
json_path = Path("sample_data/GHSaspirin.json")
with open(json_path, "r", encoding="utf-8") as f:
    datos = json.load(f)

def ghs_parsing(ghs_data):
    record = main.ghs_info.get("Record", {})
    sections = record.get("Section", [])
    sub_section = sections.get("Section", [])
    information = sub_section.get("Information", [])
    for section in sections:




# Lots of work to be done
