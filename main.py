import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompt import system_prompt
from call_functions import available_functions, call_function

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
    model='gemini-2.5-flash-lite', contents=messages,
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


function_responses_parts = []
if function_calls is not None:
    for function_call in function_calls:
        # 1. Call the function
        function_call_result = call_function(function_call, verbose=args.verbose)
        # 2. Safety Checks make sure we received result
        if function_call_result.parts is None:
            raise Exception("Error: no parts in function call result")
        if function_call_result.parts[0].function_response is None:
            raise Exception("Error: no function response in first part")
        if function_call_result.parts[0].function_response.response is None:
            raise Exception("Error no actual response from result")
        function_responses_parts.append(function_call_result.parts[0])

        if args.verbose:
            print(f"-> {function_call_result.parts[0],function_call_result.parts[0].function_response.response}")
else:
    print(response.text)