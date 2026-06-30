from fastapi import FastAPI
app = FastAPI()

@app.get('/student')
def student(name:str,age:int):
    return {
        "Name" : name,
        "Age" : age
    }