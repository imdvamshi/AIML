from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class House(BaseModel):
    area : int
    bedrooms : int
    bathrooms : int
    ready_to_move : bool

@app.post("/housepriceprediction/")
def house(data:House):
    return {
        "Area" : data.area,
        "Bedrooms" : data.bedrooms,
        "Bathrooms" : data.bathrooms,
        "ready_to_move" : data.read_to_move
    }