import os
import time
import openai

api_key = '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'
lang = 'en'
openai.api_key = api_key
messages = [{"role":"user", "content": ""}]

while True:
    
    message = input("user : ")
    messages.append( { "role": "user" , "content" : message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(reply)

        