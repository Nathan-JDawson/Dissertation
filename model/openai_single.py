import openai # type: ignore
import config # type: ignore

cfg = config.Config("main.cfg")

openai.api_key = cfg["OPENAI_API_KEY"]

openai.Completion.create

openai.Completion

if __name__ == "__main__":
    prompt = input("Prompt: ")

    response = openai.Completion.create(
        model="ada:ft-personal:new-ada-200-2022-06-01-20-27-04",
        prompt=prompt + " ->",
        stop=" END",
        temperature=0.1,
        max_tokens=250,
        presence_penalty=1.8,
        frequency_penalty=1.8
    )

    print(response["choices"][0]["text"])
# endif