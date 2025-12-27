import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompt import system_prompt
from call_functions import available_functions

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

parser = argparse.ArgumentParser(description="AI Coding Agent practice")
parser.add_argument("prompt", type=str, help="Put a prompt here")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()


messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]


if api_key is None:
    raise RuntimeError("Gemini API Key not found")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], 
        system_instruction=system_prompt),
)

function_calls = response.function_calls
metadata = response.usage_metadata

if metadata is None:
    raise RuntimeError("Failed API request")
if args.verbose:
    print("User prompt: {args.prompt}}")
    print(f"Prompt tokens: {metadata.prompt_token_count}")
    print(f"Response tokens: {metadata.candidates_token_count}")

if function_calls is not None:
    for function_call in function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
else:
    print(response.text)