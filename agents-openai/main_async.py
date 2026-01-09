import asyncio

from agents import Agent, Runner

async def main():
    agent = Agent(
        name="City information Assistant",
        instructions="You are a helpful assistant that provides information about cities."
    )

    result = await Runner.run(
        agent,
        "Suggest a budget for a trip to New York City."
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())