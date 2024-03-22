from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
# Import your promptResponse function with the new signature
from app.middleware.processPrompt import promptResponse

app = FastAPI()

# Setup the templates directory
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    """
    Render the form for user input. Initially, there's no response to display.
    """
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def process_form(request: Request, prompt: str = Form(...), interest: str = Form(...), budget: float = Form(0.0)):
    """
    Process the form submission. Takes user's prompt, interest area, and budget to generate a response.
    """
    # Generate a response based on the prompt, interest, and budget
    newResponse = promptResponse(prompt, interest, budget)
    # Render the same form template but with the new response included for display
    return templates.TemplateResponse("form.html", {"request": request, "response": newResponse})

# Update your processPrompt.py's promptResponse function to handle the new parameters.
# This example assumes you'll modify it accordingly to use the interest and budget for generating recommendations.

