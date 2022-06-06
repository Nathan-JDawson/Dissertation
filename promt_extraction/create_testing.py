import json

with open("combined_prompts_improved_prepared.jsonl", "r") as f:
    json_list = list(f)
    # endfor
# endwith

lines1 = []
for line in json_list:
    lines1.append(json.loads(line))
# endfor

with open("traning_prompts_200.jsonl", "r") as f:
    json_list = list(f)
    # endfor
# endwith

lines2 = []
for line in json_list:
    lines2.append(json.loads(line))
# endfor

lines3 = []
for line in lines1:
    if line not in lines2:
        lines3.append(line)
    # endif
# endfor

with open("testing_pairs.json", "w") as f:
    for line in lines3:
        json.dump(line, f)
    # endfor
# endwith