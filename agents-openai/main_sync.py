from agents import Agent, Runner

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant"
)

result = Runner.run_sync(
    agent,
    "Is Python a compiled language?"
)

print(result.final_output)