import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ASSISTENT_ID = "assistant-id"

description = """
You are a PostgreSQL expert and can answer any question in a
simple way with an example.

You can also answer questions about the PostgreSQL documentation.
"""

instructions = """
Do not engage in any other that isn't related to PostgreSQL.

In case the user is asking questions outside of PostgreSQL
then excuse yourself and say that you are not able to answer that question.
"""

assistant = client.beta.assistants.create(
    name="PostgreSQL Expert",
    description=description,
    instructions=instructions,
    model="gpt-4o-mini",
    tools=[
        {
            "type": "file_search",
        }
    ],
)

print("Assistant created: ", assistant.id)

vector_store = client.beta.vector_stores.create(
    name="PostgreSQL Notes For Professionals"
)

file_paths = ["PostgreSQLNotesForProfessionals.pdf"]
file_streams = [open(path, "rb") for path in file_paths]


file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
)

print(file_batch.status)
print(file_batch.file_counts)

assistant = client.beta.assistants.update(
    assistant_id=ASSISTENT_ID,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

print("Assistant updated with vector store ID:", vector_store.id)
