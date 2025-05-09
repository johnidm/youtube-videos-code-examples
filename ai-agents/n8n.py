from fastapi import FastAPI, Body
import httpx

app = FastAPI()


@app.get("/send")
def send():
    url = "http://localhost:5678/webhook/f4c8788e-34c4-4421-8e8c-426817eb0d51"
    httpx.post(url, data={"message": "What is the capital of France?"})


@app.post("/receive")
def receive(body: dict = Body(...)):
    print(body)
    

