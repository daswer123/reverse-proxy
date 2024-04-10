import os
from openai import OpenAI
from anthropic import Anthropic

# OpenAI
async def request_openai(api_keyy,messagess,modell):
    client = OpenAI(
        api_key=api_keyy
    )

    chat_completion = client.chat.completions.create(
        messages=messagess,
        model=modell,
        max_tokens=1024
    )
    
    return chat_completion.choices[0].message.content

async def request_claude(api_keyy,messagess,modell):
    
    claude = Anthropic(
        api_key=api_keyy
    )
    
    req = claude.messages.create(
    model=modell,
    max_tokens=1024,
    messages=messagess
    )
    
    output = req["content"][0]["text"]
    return output
