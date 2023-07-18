import os
import openai
from config import API_key

openai.api_key = API_key

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an email to the boss for regisnation",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)