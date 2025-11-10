# app.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib

# Load model
model = joblib.load("model.pkl")

app = FastAPI(title="Iris Model Web App")

# Set up templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    sepal_length: float = Form(...),
    sepal_width: float = Form(...),
    petal_length: float = Form(...),
    petal_width: float = Form(...)
):
    # Prepare data
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    pred = model.predict(features)[0]
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction": int(pred)}
    )
