import json
from rouge_score import rouge_scorer # type:ignore
from typing import Dict

with open("completions.json", "r") as f:
    completions = json.load(f)
# endwith

with open("testing_pairs.json", "r") as f:
    tests = json.load(f)
# endwith

rouge_totals: Dict[str, int] = {}
for line in completions:
    prompt = line["prompt"]
    check = line["completion"].replace(",", "").replace(".", "").replace("(", "").replace(")", "")
    
    for test in tests:
        if test["prompt"] == prompt:
            reference = test["completion"]
        # endif
    # endfor

    scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rouge3", "rouge4"], use_stemmer=True)
    score = scorer.score(reference, check)

    if line["model"] in rouge_totals:
        rouge_totals[line["model"]] += (score["rouge1"][-1] * 0.25) + (score["rouge2"][-1] * 0.25) + (score["rouge3"][-1] * 0.25) + (score["rouge4"][-1] * 0.25)
    else:
        rouge_totals[line["model"]] = (score["rouge1"][-1] * 0.25) + (score["rouge2"][-1] * 0.25) + (score["rouge3"][-1] * 0.25) + (score["rouge4"][-1] * 0.25)
    # endif

    print(rouge_totals)
# endfor

# print(rouge_totals)
for key in rouge_totals.keys():
    print(key + ":" + format(rouge_totals[key], ".1f"))