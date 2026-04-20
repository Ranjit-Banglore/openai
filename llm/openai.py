from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

def openai(prompt: str):
    response=client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )

    return response