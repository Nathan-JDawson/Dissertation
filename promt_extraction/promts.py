from docx import Document # type: ignore
from os import listdir
from os.path import isfile, join
from typing import List, Dict
import json

# get list of every file in the directory
path = "../example_reports"
files = [f for f in listdir(path) if isfile(join(path, f))]

json_list: List[Dict[str, str]] = []

# the reports are not consistent with how they name the results section
# this list contains all the headings of the sections that need to be extracted
accepted_headings: List[str] = [
                                    "Survey Results",
                                    "BUilding survey results",
                                    "survey results",
                                    "SURVEY results",
                                    "BUILDING INSPECTION RESULTS",
                                    "BAt Inspection survey results",
                                    "BATS: BUilding survey results",
                                    "BAT BUILDING INSPECTION",
                                    "survey RESULTS",
                                    "BatS: BUilding survey results"
                                ]

for f in files:
    doc = Document(join(path, f))
    styles = doc.styles
    paragraphs = doc.paragraphs

    # json_text = {'file':f}
    # json_list.append(json_text)

    results_text = False

    for para in paragraphs:
        if para.style.name == "Simply Heading" and results_text and para.text not in accepted_headings:
            results_text = False
        # endif
        if para.style.name == "Simply Heading" and para.text in accepted_headings:
            results_text = True
            # json_text = {'header':para.text}
            # json_list.append(json_text)
        # endif
        if results_text and "." in para.text and para.style.name == "General text" and "Plate" not in para.text.split(' ', 1)[0]:
            # split paragraph on fullstop and but keeps fullstop in sentence
            d = ". "
            para_list = [p+d for p in para.text.split(d) if p]
            
            for p in para_list:
                print(p)
                answer = input("Keep?\n")

                if answer == "y":
                    json_text = {'prompt':'->', 'completion':' ' + p}
                    json_list.append(json_text)
                # endif
            # endfor
        #endif
    # endfor
# endfor

with open("example_prompts.json", "w") as json_file:
    json.dump(json_list, json_file)
# endwith