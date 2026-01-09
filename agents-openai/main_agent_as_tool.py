import asyncio

from agents import Agent, Runner
from agents import AgentHooks

class LogHooks(AgentHooks):
    async def on_start(self, context, agent):
        print(f"Agent starting: {agent.name}")

    async def on_end(self, context, agent, output):
        print(f"Agent finished: {agent.name} → {output}")

product_agent_agent = Agent(
    name="Product Agent Review",
    instructions="You are a product agent review. You review the product and provide a review.",
    hooks=LogHooks(),
)
trip_planner_agent = Agent(
    name="Trip Planner Agent",
    instructions="You are a trip planner agent. You plan trips and provide recommendations.",
    hooks=LogHooks(),
)
orchestrator_agent = Agent(
    name="Orchestrator Agent",
    instructions=(
        "You are an orchestrator agent. You use the tools given to you to help the user." 
    ),
    hooks=LogHooks(),
    tools=[
        product_agent_agent.as_tool(
            tool_name="review_product",
            tool_description="Review the product and provide a review.",
        ),
        trip_planner_agent.as_tool(
            tool_name="plan_trip",
            tool_description="Plan a trip and provide recommendations.",
        ),

    ],
)

async def main():
    while True:
        user_input = input("User (ENTER to exit): ")

        if user_input == "":
            break

        result = await Runner.run(orchestrator_agent, input=user_input)
        print(result.final_output[:50] + "...")


if __name__ == "__main__":
    asyncio.run(main())
