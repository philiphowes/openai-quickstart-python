import os
import openai

OPENAI_API_KEY="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"

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

print(openai.api_key)

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)