from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import numpy as np

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount("/static",StaticFiles(directory='static'),name="static")

@app.get("/",response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

class Home(BaseModel):
    area : float
    bedrooms : int
    bathrooms : int

@app.post("/predict")
def predict(data:Home):
    # features = np.array([[data.area],[data.bedrooms],[data.bathrooms]])
    # prediction = model.predict(features)
    ans = data.area+ data.bedrooms + data.bathrooms
    return {
        "prediction" : ans
    }




