from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():

    env = os.getenv("APP_ENV")

    return {"message": "Hello, World!", "env": env}
