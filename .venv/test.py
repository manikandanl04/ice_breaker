import os
from dotenv import load_dotenv
import openai 

env_file = 'config.env'  # Replace with your custom filename\n",
load_dotenv(env_file)    # Load the environment file\n",

#openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
		max_tokens = 700,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

prompt = "What is the capital of india"
response = get_completion(prompt)
print(response)