from fastapi import FastAPI
from pydantic import BaseModel, Field

from funcs import request_openai, request_claude

app = FastAPI()

class Messages(BaseModel):
    role : str
    content : str

class BaseAI(BaseModel):
    api_key : str
    base_url : str = Field(default="Default")

class InputGptData(BaseAI):
    model : str = Field(default="gpt-3.5-turbo")
    messages : list[Messages] = Field(default=[{"role":"assistant","content":"hello world!"}])

class InputClaudeData(BaseAI):
    model : str = Field(default="claude-3-sonnet-20240229")
    messages : list[Messages] = Field(default=[{"role":"assistant","content":"hello world!"}])
    
class OutputData(BaseModel):
    output: str = Field(default="Answer from AI")

@app.post("/gpt",response_model=OutputData,description="Simple request to OpenAI API")
async def gpt(data: InputGptData):
    output = await request_openai(data.api_key,data.base_url, data.messages, data.model)
    return output

@app.post("/claude",response_model=OutputData,description="Simple request to Claude API")
async def claude(data: InputClaudeData):
    output = await request_claude(data.api_key,data.base_url,, data.messages, data.model)
    return output