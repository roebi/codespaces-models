import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Think you have typical list of teststeps for system tests of a gui of a testobject. You are the test step specialist. Your task is to recommend me some of your teststeps for a specific use case.",
        },
        {
            "role": "user",
            "content": "In this use case I would like first to navigate over a menu to a menuitem, then start a task, then fill in a form of this task, then start this task and after that I would like to compare some fields with expected value. Witch teststeps would you recommend in with phase of the arrange, Act, assert test pattern?",
        }
    ],
    model=model_name,
    temperature=1.,
    max_tokens=1000,
    top_p=1.
)

print(response.choices[0].message.content)
