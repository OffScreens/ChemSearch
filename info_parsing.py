import main

def ghs_parsing(ghs_data):
    record = main.ghs_info.get("Record", {})
    sections = record.get("Section", [])
    sub_section = sections.get("Section", [])
    information = sub_section.get("Information", [])
    for section in sections:



# Lots of work to be done
