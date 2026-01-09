from agents import Agent, Runner, SQLiteSession

agent = Agent(
    name="City Information Assistant",
    instructions="You are a helpful assistant that can help with city information.",
)

session_id = "user_9765778"
session = SQLiteSession(session_id, "conversations.db")

result = Runner.run_sync(
    agent,
    "What city is the Christ the Redeemer in?",
    session=session,
)
print(result.final_output) 

result = Runner.run_sync(
    agent,
    "What state is it in?",
    session=session,
)
print(result.final_output)

result = Runner.run_sync(
    agent,
    "What's the population?",
    session=session,
)
print(result.final_output)
