"""Test env for python."""

from elevenlabs import generate, stream, set_api_key
import os
import openai
import nltk.data
import time

openai.organization = os.environ.get("organization_key")
openai.api_key = os.environ.get("openai_key")
set_api_key(os.environ.get("elevenlabs_key"))

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def get_user_input():
    user_input = input("Enter a prompt: ")
    return user_input
  

def response_to_token_stream(response):
    for chunk in response:
        delta = chunk.choices[0].delta
        content = delta.content if hasattr(delta, "content") else ""
        yield content

def token_to_sentence_stream(token_iter):
    sentence = []
    for token in token_iter:
        sentence.append(token)
        if token.endswith('.') or token.endswith('?') or token.endswith('!'):
            s = ''.join(sentence)
            print(s)
            print(time.time_ns())
            yield s
            sentence = []


while True:
    user_prompt = get_user_input()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_prompt}],
        max_tokens=4000,
        temperature=0,
        stream=True
    )

    audio_stream = generate(
        text=token_to_sentence_stream(response_to_token_stream(response)),
        stream=True,
        voice="Matilda",
        model="eleven_multilingual_v2"
    )

    print("stream")
    stream(audio_stream)

# print(openai.Model.list())