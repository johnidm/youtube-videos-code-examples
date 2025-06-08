import sys
from openai import OpenAI
import base64
from pydantic import BaseModel
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class DataExtractor(BaseModel):
    name: str
    email: str


def main(file_name: str):
    with open(file_name, "rb") as file:
        file_data = file.read()
        base64_data = base64.b64encode(file_data).decode("utf-8")

    response = client.beta.chat.completions.parse(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are a expert to extract data from a PDF files.",
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "PDF file:",
                    },
                    {
                        "type": "file",
                        "file": {
                            "file_data": "data:application/pdf;base64," + base64_data,
                            "filename": file_name,
                        },
                    },
                ],
            },
        ],
        response_format=DataExtractor,
    )

    data: DataExtractor = response.choices[0].message.parsed
    print("Tokens usage:")
    print(f" - Completion tokens: {response.usage.completion_tokens}")
    print(f" - Prompt tokens: {response.usage.prompt_tokens}")
    print(f" - Total tokens: {response.usage.total_tokens}")
    print("-" * 100)
    print("Extracted data:")
    print(data)


if __name__ == "__main__":
    file_name = sys.argv[1]
    main(file_name)
