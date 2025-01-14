import openai
import time
from functools import lru_cache
from dataclasses import dataclass
import os


openai.api_key = os.getenv("OPENAI_API_KEY")


USER = "user"
ASSISTANT = "assistant"


@dataclass
class Message:
    actor: str
    payload: str


@lru_cache
def get_assistant_id(name: str) -> str:
    assistants = openai.beta.assistants.list()

    for assistant in assistants:
        if assistant.name == name:
            return assistant.id

    raise Exception(f"Assistant {name} not found")


@lru_cache
def get_thread_id(thread_id: str = None):
    if not thread_id:
        return openai.beta.threads.create()

    return thread_id


def get_thread_messages(thread_id: str):
    try:
        messages = openai.beta.threads.messages.list(thread_id, order="asc")
        return messages

    except openai.NotFoundError:
        return []


def get_history_messages(thread_id: str):
    history = []

    messages = get_thread_messages(thread_id)

    for message in messages:
        role = message.role
        for content in message.content:
            history.append(Message(actor=role, payload=content.text.value))

    return history


def get_chat_response(assistant_id: str, thread_id: str, prompt: str):
    openai.beta.threads.messages.create(
        thread_id=thread_id,
        content=prompt,
        role="user",
    )

    run = openai.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )

    print(f"Run created: {run.id}")

    while run.status != "completed":
        run = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        time.sleep(0.3)
    else:
        print("Run completed")

    messages = openai.beta.threads.messages.list(thread_id=thread_id)
    return messages.data[0].content[0].text.value.strip()
