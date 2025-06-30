from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import uvicorn

# Initialize FastAPI
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Model credentials
HUGGINGFACE_TOKEN = "your_huggingface_token_here"
model_id = "ibm/granite-3b-instruct"

# Load IBM Granite Model
tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=HUGGINGFACE_TOKEN)
model = AutoModelForCausalLM.from_pretrained(model_id, use_auth_token=HUGGINGFACE_TOKEN)
ai_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Demo credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"

@app.get("/", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return RedirectResponse("/home", status_code=302)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

@app.get("/home", response_class=HTMLResponse)
def home_page(request: Request):￼Enter
