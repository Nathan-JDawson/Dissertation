import json
from typing import Any, List

with open("evaluation_completions.json", "r") as f:
    data = json.load(f)
# endwith

collection = []
same_p: List[Any] = []

for i, d in enumerate(data):
    if i % 4 == 0:
        collection.append(same_p)
        same_p = []
    # endif
    same_p.append([d["completion"], d["model"]])
# endfor
collection.append(same_p)


for group in collection:
    for c in group:
        print(c[0] + c[1] + "\n")
    # endfor
    input()
# endfor