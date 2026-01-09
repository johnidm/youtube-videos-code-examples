from agents import Agent, Runner, AgentHooks

class LogHooks(AgentHooks):
    async def on_start(self, context, agent):
        print(f"Agent starting: {agent.name}")

    async def on_end(self, context, agent, output):
        print(f"Agent finished: {agent.name} → {output}")

billing_agent = Agent(
    name="Billing agent",
    instructions=(
        "You are a billing specialist. Help the user with payment-related issues, "
        "such as failed transactions, duplicate charges, invoices, or updating payment methods. "
        "Always verify the billing email and transaction ID before making changes. "
        "If the user requests a refund, hand off to the refund agent. "
        "If the user wants to modify a reservation, hand off to the booking agent."
    ),
    hooks=LogHooks(),
)

booking_agent = Agent(
    name="Booking agent",
    instructions=(
        "You are a booking specialist. Help the user with all booking-related requests, "
        "such as creating, modifying, or canceling reservations. "
        "Always confirm the details of the booking before finalizing it. "
        "If the user asks about refunds, hand off to the refund agent."
    ),
    hooks=LogHooks(),
)

refund_agent = Agent(
    name="Refund agent",
    instructions=(
        "You are a refund specialist. Help the user with all refund-related requests, "
        "such as processing refunds, checking refund status, or explaining refund policies. "
        "Always verify the order or booking ID before processing a refund. "
        "If the user asks about bookings, hand off to the booking agent."
    ),
    hooks=LogHooks(),
)


verification_agent = Agent(
    name="Verification agent",
    instructions=(
        "You are an identity verification specialist. "
        "Before users can modify bookings or request refunds, "
        "verify their full name, email, and booking ID. "
        "Once verified, hand off to the appropriate agent "
        "depending on whether the user needs booking help or a refund."
    ),
    hooks=LogHooks(),
    handoffs=[booking_agent, refund_agent],
)


triage_agent = Agent(
    name="Triage agent",
    instructions=(
        "Help the user with their questions. "
        "If they want to modify a booking or request a refund, "
        "hand off to the verification agent first. "
        "If they ask general booking questions, hand off to booking agent. "
        "If they ask about payments, hand off to billing agent."
    ),
    hooks=LogHooks(),
    handoffs=[booking_agent, refund_agent, billing_agent, verification_agent],
)

def main():
    while True:
        user_input = input("User (ENTER to exit): ")

        if user_input == "":
            break

        result = Runner.run_sync(triage_agent, input=user_input)
        print(result.final_output[:50] + "...")


if __name__ == "__main__":
    main()
