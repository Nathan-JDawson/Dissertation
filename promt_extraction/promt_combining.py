import json
import re

def check_duplicate(x1, x2):
    for n1 in x1:
        for n2 in x2:
            if n1 == n2:
                return True
            # endif
        # endfor
    # endfor
    return False

# replaces all doubles space with one space and puts space after each fullstop
def one_space(s):
    return re.sub('\.(?! )', '. ', re.sub(' +', ' ', s))

with open("./extracted_prompts.json", "r") as f:
    data = json.load(f)
# endwith

prompt_collection = []
for d1 in data:
    d3 = d1
    delimit = "."
    suffix = " END"
    prompts1 = [p + delimit for p in d1["prompt"].split(delimit)][:-1]
    for d2 in data:
        if d1 != d2:
            prompts2 = [p + delimit for p in d2["prompt"].split(delimit)][:-1]
            dup = check_duplicate(prompts1, prompts2)
            if len(d3["prompt"].split(delimit)) > 5:
                if suffix not in d3["completion"]:
                    d3["completion"] += suffix
                prompt_collection.append(d3)
                d3 = d1
            # endif
            if not dup:
                d3 = {"prompt":"".join(prompts1) + "".join(prompts2) + "->", "completion":d3["completion"] + d2["completion"]}
            # endif
        # endif
    # endfor
    if suffix not in d3["completion"]:
        d3["completion"] += suffix
    prompt_collection.append(d3)
# endfor

for p in prompt_collection:
    p["prompt"] = one_space(p["prompt"])

with open("combined_prompts.json", "w") as f:
    json.dump(prompt_collection, f)