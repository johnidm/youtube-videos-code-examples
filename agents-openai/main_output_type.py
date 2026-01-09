from pydantic import BaseModel
from agents import Agent, Runner

class CakeRecipe(BaseModel):
    name: str
    steps: list[str]
    ingredients: list[str]
    original_input: str

agent = Agent(
    name="Recipe Cake Agent",
    instructions="You are a cake recipe expert.",
    output_type=CakeRecipe,
)

result = Runner.run_sync(
    agent,
    "I want to make a chocolate cake.",
)

recipe = result.final_output
print(recipe.name)
print(recipe.steps)
print(recipe.ingredients)
print(recipe.original_input)


