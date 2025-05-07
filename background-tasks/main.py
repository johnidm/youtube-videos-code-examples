import httpx
from fastapi import BackgroundTasks, FastAPI

app = FastAPI(title="Background Tasks Example")


def answer_question(email: str, question: str):
    print(f"Answering question for {email}: {question}")
    answer = f"This is my answer for your question: {question}"

    httpx.post("http://localhost:8000/answer", json={"email": email, "answer": answer})


@app.post("/ask")
async def send_notification(
    email: str, question: str, background_tasks: BackgroundTasks
):
    print(f"Sending question for {email}: {question}")
    background_tasks.add_task(answer_question, email, question)
    return {"message": "Notification sent in the background"}


@app.post("/answer")
async def answer(email: str, answer: str):
    print(f"Answered for {email}: {answer}")
    return {"message": f"Answered for {email}: {answer}"}
