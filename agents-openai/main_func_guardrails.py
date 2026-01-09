import json

from agents import (
    Agent,
    Runner,
    ToolGuardrailFunctionOutput,
    function_tool,
    tool_input_guardrail,
    tool_output_guardrail,
)


@tool_input_guardrail
def block_restricted_queries(data) -> ToolGuardrailFunctionOutput:
    args = json.loads(data.context.tool_arguments or "{}")
    query = str(args.get("product_name", "")).lower()
    restricted_terms = ["weapon", "explosive", "illegal"]
    if any(term in query for term in restricted_terms):
        return ToolGuardrailFunctionOutput.reject_content(
            f"Search blocked: '{query}' is a restricted term."
        )
    return ToolGuardrailFunctionOutput.allow()


@tool_output_guardrail
def filter_expensive_products(data) -> ToolGuardrailFunctionOutput:
    try:
        products = json.loads(data.output or "[]")
        filtered = [p for p in products if p.get("price", 0) <= 500]
        print(filtered)
        if not filtered:
            return ToolGuardrailFunctionOutput.reject_content(
                "No products found within the allowed price range."
            )
        return ToolGuardrailFunctionOutput.replace_content(json.dumps(filtered, indent=2))
    except Exception:
        return ToolGuardrailFunctionOutput.allow()


@function_tool(
    tool_input_guardrails=[block_restricted_queries],
    tool_output_guardrails=[filter_expensive_products],
)
def search_products(product_name: str) -> str:
    return json.dumps(
        [
            {"title": "Sample phone", "price": 300},
            {"title": "Expensive laptop", "price": 1500},
            {"title": "Legal weapon", "price": 1000},
        ]
    )


agent = Agent(
    name="Product Finder Assistant",
    instructions="Help users find products. Use the search tool to look up items.",
    tools=[search_products],
)


def main():
    result = Runner.run_sync(agent, "Find a laptop")
    print(result.final_output)


if __name__ == "__main__":
    main()
