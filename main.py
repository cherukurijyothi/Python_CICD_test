from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Test from FastAPI from Jenkins to server -123"}
