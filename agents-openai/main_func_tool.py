import json
import asyncio
import requests
from agents import Agent, function_tool, Runner


@function_tool  
async def search_products(product_name: str) -> str:
    """Search for 10 products by name.
    Args:
        product_name: The name of the product to search for.
    """
    print(f"Searching for products with name: {product_name}")

    url = f"https://dummyjson.com/products/search?q={product_name}&limit=10"
    response = requests.get(url)
    response.raise_for_status()
    products = response.json().get("products", [])
    products_info = [
        {
            "title": product["title"],
            "price": product["price"],
        }
        for product in products
    ]

    if not products_info:
        return "No products found"
    
    return json.dumps(products_info, indent=2)

agent = Agent(
    name="Product Finder Assistant",
    tools=[search_products],  
)

async def main():
    while True:
        user_input = input("User (ENTER to exit): ")

        if user_input == "":
            break

        result = await Runner.run(agent, input=user_input)
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
