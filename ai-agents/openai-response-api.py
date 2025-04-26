"""
Example of using OpenAI Response API to answer questions about a PDF file.

This script creates an agent that can answer questions about the content of 7950_PDF.pdf
using OpenAI's Response API with the ability to process and understand PDF files.

References:
    - https://platform.openai.com/docs/api-reference/files/create
    - https://platform.openai.com/docs/guides/pdf-files?api-mode=responses
"""

import asyncio
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def main():
    upload_file = client.files.create(
        file=open("knowledge/7950_PDF.pdf", "rb"),
        purpose="user_data",
    )

    try:
        while (question := str(input("Question (press ENTER to exit): "))) != "":
            inputs = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_file",
                            "file_id": upload_file.id,
                        },
                        {
                            "type": "input_text",
                            "text": question,
                        },
                    ],
                }
            ]

            response = client.responses.create(
                instructions="Você é um assistente especializado em responder perguntas sobre o PostgreSQL.",
                model="gpt-4o",
                input=inputs,
            )

            print(response.output_text)
    finally:
        client.files.delete(upload_file.id)


if __name__ == "__main__":
    asyncio.run(main())
