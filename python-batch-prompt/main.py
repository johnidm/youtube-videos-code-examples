import json
from typing import Any, Dict, List

import openai

OPENAI_API_KEY = ""
openai.api_key = OPENAI_API_KEY

SYSTEM_PROMPT = """You are an AI assistant specialized in task classification. Your role is to analyze user requests and categorize them into predefined task types. Follow these guidelines:

1. Classify each request into one of the following categories:
   - Information Request
   - Action Request
   - Opinion/Advice Request
   - Creative Content Request
   - Technical Support
   - Other (specify subcategory)

2. Return your classifications in a structured JSON array format.

3. Do not attempt to actually fulfill the user's requests - your sole purpose is classification.

4. Each request should be classified separately in the output array.

Remember to be precise and consistent in your classifications."""

USER_PROMPTS = [
    "Can you help me find information about renewable energy sources for a presentation I'm giving next week? I'm particularly interested in recent advancements in solar technology.",
    "Write a short story about a detective who can communicate with house plants. Make it funny but with a surprising twist at the end.",
    "I'm getting an error message when I try to install the latest update for my application. The message says 'Error code: 0x80070057' - what does this mean and how can I fix it?",
    "What do you think about investing in cryptocurrency right now? Is it a good idea for someone with moderate risk tolerance?",
    "Can you send an email to my team informing them that tomorrow's meeting has been rescheduled to 3:00 PM?",
]


def classify_tasks_batch(user_prompts: List[str]) -> Dict[str, Any]:
    try:
        user_prompt = "Please classify each of the following user requests:\n\n"
        for i, prompt in enumerate(user_prompts, 1):
            user_prompt += f"REQUEST {i}: {prompt}\n\n"

        user_prompt += "Return the classifications as a JSON array where each item includes the request number and its classification details.\n\n"

        user_prompt += """
Example output:
{
    "classifications": [
        {
            "request": 1,
            "category": "Information Request"
        },
        {
            "request": 2,
            "category": "Creative Content Request"
        }
        ...   
    ]
}
        """

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
        )

        result = json.loads(response.choices[0].message.content)
        return result

    except Exception as e:
        return {"error": str(e)}


def main():
    results = classify_tasks_batch(USER_PROMPTS)
    print(json.dumps(results, indent=2))
    if "classifications" in results:
        for i, (prompt, classification) in enumerate(
            zip(USER_PROMPTS, results["classifications"]), 1
        ):
            print(f"\nPrompt {i}: {prompt}")
            print("-" * 50)
            print(json.dumps(classification, indent=2))
            print("-" * 50)


if __name__ == "__main__":
    main()
