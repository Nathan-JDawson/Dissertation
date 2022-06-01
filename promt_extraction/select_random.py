import json
import random
from typing import List

lines = []
with open("combined_prompts_prepared.jsonl", "r") as f:
    for line in f:
        lines.append(line)
    # endfor
# endwith

max = 50

random_nums: List[int] = (random.sample(range(0, len(lines)), max))
random_nums.sort()

random_prompts = []
for num in random_nums:
    random_prompts.append(lines[num])
# endfor

with open("random_prompts_prepared_" + str(max) + ".jsonl", "w") as f:
    for p in random_prompts:
        f.write(p)
    # endfor
# endwith