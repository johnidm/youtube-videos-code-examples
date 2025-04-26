"""
https://www.datacamp.com/tutorial/openai-agents-sdk-tutorial
"""

from dotenv import load_dotenv
from openai import OpenAI
from agents import Runner, WebSearchTool, FileSearchTool, Agent, ModelSettings
import asyncio

load_dotenv()

client = OpenAI()

VECTOR_STORE_NAME = "PostgreSQL Arquivos"

vector_store = [ v for v in client.vector_stores.list() if v.name == VECTOR_STORE_NAME ]
if not vector_store:
    vector_store = client.vector_stores.create(name=VECTOR_STORE_NAME)
    print(f"Vector Store ID: {vector_store.id}")
    vector_store_id = vector_store.id

    file1 = client.files.create(
        file=open("knowledge/7950_PDF.pdf", "rb"),
        purpose="assistants"
    )

    file_ids = [
        file1.id
    ]
    
    client.vector_stores.file_batches.create(
        vector_store_id=vector_store.id,
        file_ids=file_ids   
    )
else:
    vector_store_id = vector_store[0].id

agent = Agent(
    name="PostgreSQL Assistente",
    instructions="Você é um assistente especializado em responder perguntas sobre o PostgreSQL.",
    model="gpt-4o",
    model_settings=ModelSettings(
        temperature=0.7,
        max_tokens=1024,
    ),
    tools=[
        # FileSearchTool(
        #     vector_store_ids=[vector_store_id],
        #     max_num_results=3
        # ),
        WebSearchTool(
            user_location={
                "type": "approximate",
                "country": "BR",
                "city": "Florianópolis"
            },
            search_context_size="low"
        )
    ]
)


async def main():
    while (question := str(input("Pergunta (ENTER para sair): ")).strip()) != "":
        result = await Runner.run(agent, question)
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
