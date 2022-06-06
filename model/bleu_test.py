import json
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction # type:ignore
from typing import Dict

with open("completions.json", "r") as f:
    completions = json.load(f)
# endwith

with open("testing_pairs.json", "r") as f:
    tests = json.load(f)
# endwith

bleu_totals: Dict[str,int] = {}
for line in completions:
    # extract prompt and completion and covert to arrays of strings
    prompt = line["prompt"]
    check = line["completion"]

    for test in tests:
        if test["prompt"] == prompt:
            reference = test["completion"]
        # endif
    # endfor

    reference = reference.replace("_", " ").replace(".", "").split(" ")[1:-1]
    check = check.replace(",", "").replace(".", "").replace("(", "").replace(")", "").split(" ")

    array = [reference]
    smooth = SmoothingFunction()
    score = sentence_bleu(array, check, weights=(0.25,0.25,0.25,0.25), smoothing_function=smooth.method1)
    
    if line["model"] in bleu_totals:
        bleu_totals[line["model"]] += score
    else:
        bleu_totals[line["model"]] = score
    # endif

# endfor

# print(bleu_totals)
for key in bleu_totals.keys():
    print(key + " : " + format(bleu_totals[key], ".1f"))