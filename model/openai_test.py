import openai
import config # type: ignore

cfg = config.Config("main.cfg")

openai.api_key = cfg["OPENAI_API_KEY"]

if __name__ == "__main__":
    response = openai.Completion.create(
        model="ada:ft-personal-2022-05-10-14-46-37",
        prompt="evidence is yes"
    )

    print(response["choices"][0]["text"])