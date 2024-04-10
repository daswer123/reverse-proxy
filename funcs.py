import os
from openai import OpenAI
from anthropic import Anthropic

# OpenAI
async def request_openai(api_key,messages,model):
    client = OpenAI(
        api_key=api_key
    )

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        max_tokens=2048
    )
    
    return chat_completion.choices[0].message.content

async def request_claude(api_key,messages,model):
    
    claude = Anthropic(
        api_key=api_key
    )
    
    req = claude.messages.create(
    model=model,
    max_tokens=2048,
    messages=messages
    )
    
    output = req["content"][0]["text"]
    return output
