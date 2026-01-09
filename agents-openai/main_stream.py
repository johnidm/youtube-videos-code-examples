import asyncio

from agents import Agent, Runner

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant"
    )

    result = Runner.run_streamed(
        agent,
        "how can I get to New York City?"
    )

    async for event in result.stream_events():
        print(event)

if __name__ == "__main__":
    asyncio.run(main())