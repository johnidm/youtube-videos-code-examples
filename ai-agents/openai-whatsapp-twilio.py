"""
https://www.twilio.com/docs/whatsapp
"""

from dotenv import load_dotenv
from fastapi import FastAPI
from twilio.twiml.messaging_response import MessagingResponse
from fastapi import Form
from fastapi.responses import Response
from fastapi import Request
from agents import Agent, ModelSettings, WebSearchTool
from agents import Runner
from fastapi.exceptions import HTTPException
from twilio.request_validator import RequestValidator
import os
from twilio.rest import Client
from fastapi import BackgroundTasks


load_dotenv()


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)


instructions = """
Você é um assistente especializado em responder perguntas sobre o ConstruSummit 2025.

Seja sempre educado e respeitoso.
As respostas devem ser em PORTUGUÊS do Brasil.
As respostas devem ter no máximo 100 palavras.
O formato de resposta deve ser simples e direto sem nenhum tipo de formatação.
"""


client = Client(account_sid, auth_token)

agent = Agent(
    name="ConstruSummit 2025 Assistente",
    instructions=instructions,
    model="gpt-4o",
    model_settings=ModelSettings(
        temperature=0,
        max_tokens=1024,
    ),
    tools=[
        WebSearchTool(
            user_location={
                "type": "approximate",
                "country": "BR",
                "city": "Florianópolis",
            },
            search_context_size="high",
        )
    ],
)

app = FastAPI()


async def replay(message: str, to: str):
    form_ = "whatsapp:+14155238886"

    result = await Runner.run(agent, message)
    message = result.final_output

    client.messages.create(
        body=message,
        from_=form_,
        to=to,
    )


@app.post("/ask/webhook")
async def chat(
    background_tasks: BackgroundTasks,
    From: str = Form(...),
    Body: str = Form(...),
    request: Request = None,
):
    validator = RequestValidator(os.environ["TWILIO_AUTH_TOKEN"])
    form_ = await request.form()
    if not validator.validate(
        str(request.url), form_, request.headers.get("X-Twilio-Signature", "")
    ):
        raise HTTPException(status_code=400, detail="Error in Twilio Signature")

    response = MessagingResponse()
    background_tasks.add_task(replay, Body, From)
    return Response(content=str(response), media_type="application/xml")
