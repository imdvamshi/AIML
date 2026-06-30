from fastapi import FastAPI
app = FastAPI()

@app.get("/student/{id}")
def student(id:int):
    return {
        "Student id" : id
    }