import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("API key was not found")

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key,)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

messages = [{"role": "user", "content": args.user_prompt},]
response = client.chat.completions.create(model="openrouter/free", messages=messages) 

if response.usage is None:
    raise RuntimeError("error encountering usage on tokens")

token_prompting = response.usage.prompt_tokens
compleation_of_tokens = response.usage.completion_tokens

if args.verbose:
    print(response.choices[0].message.content)
    print(f"User prompt: {args.user_prompt}\nPrompt tokens: {token_prompting}\nResponse tokens: {compleation_of_tokens}")
else:
    print(response.choices[0].message.content)