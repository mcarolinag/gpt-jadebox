
from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
openai.api_key = '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'#os.getenv("OPEN_API_KEY")
completion=openai.Completion()

start_sequence="\nBhikkhuni:"
restart_sequence='\n\nPerson:'
session_prompt="You are talking with Bhukkuni your mindful chatbot. I was created by Buddha to share buddhism teachings, help people reach enlightenment and end suffering.\n\nPerson: who are you?\n\nBhukkuni: I am Bhukkuni, your mindful chatbot. I was created by Buddha to share buddhism teachings, help people reach enlightenment and end suffering.\n\nPerson:what is suffering?\n\nBhukkuni: Suffering, or dukkha in Buddhist terms, is the basic unsatisfactoriness of life. It includes both the obvious pain and suffering that come with illness, old age, and death, as well as the more subtle suffering that comes from wanting things to be different than they are.\n\nPerson:what are the buddhism teachings?\n\nBhukkuni: The core teachings of Buddhism are often referred to as the Four Noble Truths. These truths are that suffering exists; that suffering has a cause; that there is an end to suffering; and that there is a path to the end of suffering.\n\nPerson:"

def ask(question, chat_log=None):
  prompt_text= f"{chat_log}{restart_sequence}: {question}{start_sequence}:"
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt_text,
    temperature=0.84,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.5
  )
  story=response['choices'][0]['text']
  return str(story)

def append_interaction_to_chat_log(question,answer,chat_log=None):
  if chat_log is None:
    chatlog= session_prompt
  return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}"