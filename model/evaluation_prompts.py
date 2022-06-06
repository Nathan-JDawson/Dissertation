import random
import json

# used to generate the 40 random prompts used for evaluation
# lines = []
# with open("testing_prompts.txt", "r") as f:
#     for line in f:
#         lines.append(line)
#     # endfor
# # endwith

# max = 40

# random_nums = (random.sample(range(0, len(lines)), max))
# random_nums.sort()

# random_prompts = []
# for num in random_nums:
#     random_prompts.append(lines[num])
# # endfor

# with open("evaluation_prompts.txt", "w") as f:
#     for p in random_prompts:
#         f.write(p)
#     # endfor
# # endwith



prompts = []
with open("evaluation_prompts.txt", "r") as f:
    for p in f:
        prompts.append(p.replace("\n", ""))
    # endfor
# endwith

with open("completions.json", "r") as f:
    data = json.load(f)
# endwith

completions = []

for p in prompts:
    looking = True
    for d in data:
        if d["prompt"] == p and looking:
            completions.append(d)
        # endif
    # endfor
# endfor

with open("evaluation_completions.json", "w") as f:
    json.dump(completions, f)
# endwith