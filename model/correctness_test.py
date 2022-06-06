import json
from typing import Dict




with open("evaluation_completions.json", "r") as f:
    data = json.load(f)
# endwith

c_scores: Dict[str, int] = {}
i_scores: Dict[str, int] = {}
for d in data:
    print(d["prompt"] + "\n" + d["completion"] + "\n")
    correct = int(input("Correct facts: "))
    incorrect = int(input("Incorrect facts: "))

    if d["model"] in c_scores:
        c_scores[d["model"]] += correct
    else:
        c_scores[d["model"]] = correct
    # endif

    if d["model"] in i_scores:
        i_scores[d["model"]] += incorrect
    else:
        i_scores[d["model"]] = incorrect
    # endif
# endfor

print(c_scores)

print(i_scores)