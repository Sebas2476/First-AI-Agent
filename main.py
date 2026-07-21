import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import *
from call_functions import *
import json
import sys

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

messages = [{"role": "user", "content": args.user_prompt}, 
            {"role": "system", "content": system_prompt},
            ]

for i in range(20):
    response = client.chat.completions.create(model="openrouter/free", messages=messages, tools=available_functions, )
    response_message = response.choices[0].message
    messages.append(response_message)

    if response.usage is None:
        raise RuntimeError("error encountering usage on tokens")

    token_prompting = response.usage.prompt_tokens
    compleation_of_tokens = response.usage.completion_tokens
        
    if response_message.tool_calls:
        for call in response_message.tool_calls:
            result_message = call_function(call, args.verbose)
            messages.append(result_message)
    else:
        print(response_message.content)
        break
else:
    print(messages.append(result_message))
    sys.exit(1)

if args.verbose:
    print(f"User prompt: {args.user_prompt}\nPrompt tokens: {token_prompting}\nResponse tokens: {compleation_of_tokens}")