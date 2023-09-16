from queries import dataset
messages = [{"role": "user" , "content" : "message"}]

import os
import time
import openai


while True:
   i=0
   message = str(input("enter query "))
   number_of_words = len(message.split())
   list_message=message.split()
#    print(number_of_words)
   for i in range(number_of_words):
      
      if (list_message[i] in dataset):
         print(dataset[list_message[i]])


   # ** INSERT CODE FOR MESSAGE ACCURACY **
#    message_acc=0
#    for word in message:
#         if word in dataset:
#             message_acc +=1
#    percent_acc= message_acc/number_of_words
#    print(dataset[message])
   

#  ** INSERT CODE FOR USING GPT **
#    messages.append( { "role": "user" , "content" : message})
#    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
#    reply = chat.choices[0].message.content
#    print(reply)


# **INSERT CODE FOR STORING USER INPUTS **

