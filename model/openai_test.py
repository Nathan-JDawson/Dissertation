import openai
import config # type: ignore

cfg = config.Config("main.cfg")

openai.api_key = cfg["OPENAI_API_KEY"]

if __name__ == "__main__":
    response = openai.Completion.create(
        model="ada:ft-personal:comined-improved-2022-05-25-00-52-07",
        prompt=input("Promt: ") + " ->",
        stop=" END",
        temperature=0.1,
        max_tokens=250,
        presence_penalty=1.8,
        frequency_penalty=1.8
    )

    print(response["choices"][0]["text"])