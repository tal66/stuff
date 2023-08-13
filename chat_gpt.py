import openai
from other import secrets # (private dir)

openai.api_key = secrets.api_key
user = "mt"
messages = []

while True:
    content = input(f'{user}: ')
    messages.append({"role": "user", "content": content})
    res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    res_msg = res['choices'][0]['message']
    print(f"\nassistant: {res_msg['content']}")
    messages.append(res_msg)
