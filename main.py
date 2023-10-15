from elevenlabs import generate, stream, set_api_key
import os
import openai
import nltk.data

openai.organization = ""
openai.api_key = ""
set_api_key("")

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": "Who won the world series in 2020?"}],
    max_tokens=4000,
    temperature=0,
    stream=True
)

def text_stream(response):
    for chunk in response:
        delta = chunk.choices[0].delta
        content = delta.content if hasattr(delta, "content") else ""
        print(content)
        yield content

audio_stream = generate(
  text=text_stream(response),
  # text=tokenizer.tokenize(text_stream(response)),
  stream=True,
  voice="Matilda",
  model="eleven_multilingual_v2"
)

stream(audio_stream)

# print(openai.Model.list())

