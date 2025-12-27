import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

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
    model='gemini-2.5-flash', contents=messages
)

if response.usage_metadata is None:
    raise RuntimeError("Failed API request")
if args.verbose:
    print("User prompt: {args.prompt}}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
print(response.text)