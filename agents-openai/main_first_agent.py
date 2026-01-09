from agents import Agent, Runner

agent = Agent(
    name="Trip Assistant",
    instructions="""You are a helpful assistant that can help with trip planning.
    You can help with things like:
    - suggesting places to visit
    - planning a budget
    - suggesting activities to do

    If the user asks for something that is not related to trip planning,
    you should politely inform them that you can only help with trip planning.
    """,
)

result = Runner.run_sync(
    agent,
    "Suggest a budget for a trip to New York City.",
)
print(result.final_output)
