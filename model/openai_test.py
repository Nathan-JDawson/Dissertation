from time import sleep
import openai
import config # type: ignore
import json

cfg = config.Config("main.cfg")

openai.api_key = cfg["OPENAI_API_KEY"]

models = [
    "davinci:ft-personal:davinci-500-2022-05-31-21-01-34", # actually 200 size, named wrong
    "ada:ft-personal:ada-50-2022-05-31-20-44-30",
    "ada:ft-personal:ada-100-2022-05-31-20-46-36",
    "ada:ft-personal:ada-200-2022-05-31-20-49-57",
    "ada:ft-personal:ada-500-2022-05-31-20-53-37"
]

prompts = []
with open("test_prompts.txt", "r") as p:
    for line in p:
        prompts.append(line)
    # endfor
# endwith

completions = []
if __name__ == "__main__":
    for model in models:
        print(model)
        for prompt in prompts:
            response = openai.Completion.create(
                model=model,
                prompt=prompt,
                stop=" END",
                temperature=0.1,
                max_tokens=250,
                presence_penalty=1.8,
                frequency_penalty=1.8
            )

            completions.append(
                {
                    "model": model, 
                    "prompt": prompt, 
                    "completion": response["choices"][0]["text"]
                }
            )

            sleep(15)
        # endfor
    # endfor
# endif

with open("completions.json", "w") as f:
    for completion in completions:
        json.dump(completion, f)
    # endfor
# endwith