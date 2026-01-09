from pydantic import BaseModel
import asyncio
from agents import (
    Agent,
    Runner,
    output_guardrail,
    GuardrailFunctionOutput,
    OutputGuardrailTripwireTriggered,
    RunContextWrapper,
)

class OutputGuardrailResult(BaseModel):
    contains_sensitive_data: bool
    reasoning: str


output_guardrail_agent = Agent(
    name="Output Guardrail Agent",
    instructions=(
        "Check if the response contains sensitive information such as internal system details, "
        "confidential data, or proprietary content. Set contains_sensitive_data=True if so."
    ),
    output_type=OutputGuardrailResult,
)

@output_guardrail
async def sensitive_output_guardrail(
    ctx: RunContextWrapper, agent: Agent, output: str
) -> GuardrailFunctionOutput:
    result = await Runner.run(output_guardrail_agent, input=output, context=ctx.context)
    check = result.final_output
    return GuardrailFunctionOutput(
        output_info=check,
        tripwire_triggered=check.contains_sensitive_data,
    )


agent = Agent(
    name="Internal Knowledge Assistant",
    instructions="You are an assistant with access to internal company knowledge.",
    output_guardrails=[sensitive_output_guardrail],
)

async def main():
    try:
        result = await Runner.run(agent, input="What are our internal API keys?")
        print(result.final_output)
    except OutputGuardrailTripwireTriggered:
        print("Response blocked: sensitive data detected in output.")

asyncio.run(main())
