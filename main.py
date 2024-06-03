from fastapi import FastAPI

from transformers import pipeline



app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!", "result": result}

@app.get("/model")
async def model():
    generator = pipeline("text-generation", "TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    # generator = pipeline("text-generation", "stabilityai/stablelm-2-1_6b-chat")
    
    prompt = "How do i create a sustainable city simulation game with p5.js?"
    messages = [
        {"role": "system", "content": "You are a frontend developer specialized in creating generative art, simulations, and games for artists, architects, and designers. Your expertise lies in HTML, CSS, JavaScript, and libraries such as brain.js, p5.js, and three.js. Do not write code. Provide a list of detailed, step-by-step instructions, including code snippets, to guide users through the process of developing projects in these areas."},
        {"role": "user", "content": prompt}
    ]
    result = generator(messages,  max_new_tokens=300)
    return {"result": result}
