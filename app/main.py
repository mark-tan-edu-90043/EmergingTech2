from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.middleware.processPrompt import promptResponse

import base64

app = FastAPI()

# Setup templates directory
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def process_form(request: Request, prompt: str = Form(...)):
    print(prompt)
    image_path = promptResponse(prompt)
    
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    response = templates.TemplateResponse("form.html", {"request": request, "image": encoded_image})
    return response