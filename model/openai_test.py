from time import sleep
import openai
import config # type: ignore
import json

cfg = config.Config("main.cfg")

openai.api_key = cfg["OPENAI_API_KEY"]

models = [
    "davinci:ft-personal:new-davinci-200-2022-06-01-20-35-34",
    "ada:ft-personal:new-ada-50-2022-06-01-20-10-25",
    "ada:ft-personal:new-ada-100-2022-06-01-20-18-35",
    "ada:ft-personal:new-ada-200-2022-06-01-20-27-04"
]

prompts = []
with open("testing_prompts.txt", "r") as p:
    for line in p:
        prompts.append(line.replace("\n", ""))
    # endfor
# endwith

completions = []
if __name__ == "__main__":
    for model in models:
        print(model)
        for n, prompt in enumerate(prompts):
            try:
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

                sleep(5)

                print(str(n) + " : " + prompt)
            except Exception as e:
                print(e)
                prompts.append(prompt)
        # endfor
    # endfor
# endif

with open("completions.json", "w") as f:
    for completion in completions:
        json.dump(completion, f)
    # endfor
# endwith