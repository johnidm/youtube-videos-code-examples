# MCP (Model Context Protocol)

The **Model Context Protocol (MCP)** is an open, universal protocol designed to securely connect AI systems—such as large language models (LLMs) and AI agents—to a wide variety of data sources, tools, and services, both local and remote. Developed and open-sourced by Anthropic in late 2024, MCP addresses the core challenge that most advanced AI models face: limited access to real-time, dynamic context outside their static training data.

MCP standardizes the way AI applications interact with external resources, replacing the need for custom, one-off integrations with a single, scalable, and secure protocol. This enables AI agents to perform more complex, context-aware tasks, such as automating business processes, updating documents, or retrieving the latest information from databases or APIs.

## Typical Use Cases

- Connecting AI assistants to business tools (e.g., Slack, GitHub, databases)[3]
- Automating workflows that span multiple applications[1][4]
- Building agentic AI that can act on real-time data and orchestrate complex tasks[1][2][4]


## Where you can find MCP server:

- https://mcp.so/
- https://glama.ai/mcp/servers
- https://modelcontextprotocol.io/examples

## MCP Architecture

MCP uses a **client-server model** with several core components:

### **Host**

- The **Host** is the main application environment where users interact and where the AI model operates.  
- Examples include an IDE like Cursor, a chatbot interface, or a desktop AI assistant (e.g., Claude Desktop)[1][4][3].
- The Host is responsible for:
  - Initializing and managing one or more MCP Clients.
  - Managing the lifecycle and context aggregation across clients.
  - Handling user authorization and decisions about what external data or tools the AI can access.
  - Presenting results and interactions to the user[1][4].
- **In summary:** The Host acts as the orchestrator, coordinating communication between the user, the AI model, and the external systems via clients.

### **Client**

- The **Client** is a component within the Host application that manages the connection to a specific MCP Server.  
- Each Client maintains a dedicated, stateful, one-to-one connection with a single Server[1][4][3].
- Key responsibilities:
  - Routing messages and requests between the Host (and thus the AI model) and its connected Server.
  - Discovering and managing the capabilities (tools, resources, prompts) exposed by the Server.
  - Negotiating protocol versions and capabilities to ensure compatibility.
  - Managing subscriptions to resources and handling notifications for updates[4].
- **In summary:** The Client is the communication bridge, ensuring secure and structured data exchange between the Host and a particular Server.

### **Server**

- The **Server** is an external program or service that exposes specific capabilities (tools, resources, prompts) via a standardized API for use by the AI model[1][3][4].
- It acts as a wrapper or adapter around external systems such as APIs, databases, or file systems, making their functionality accessible in a uniform way[1][4].
- Servers can be implemented in any language and communicate using protocols like JSON-RPC over stdio or HTTP with Server-Sent Events (SSE)[1][4].
- Key responsibilities:
  - Advertising available tools, resources, and prompts to Clients.
  - Executing requested actions or providing data when invoked by a Client.
  - Sending responses and notifications back to the Client[1][4].
- **In summary:** The Server is the provider of external capabilities, making them accessible to AI applications through the MCP standard.

### **Summary Table**

| Component      | Description                                                      | Role                                              |
|----------------|------------------------------------------------------------------|---------------------------------------------------|
| MCP Host       | Platform or app where MCP operates (e.g., Claude Desktop, IDE)   | Coordinates clients and manages security           |
| MCP Client     | AI application or agent (e.g., Claude, Cursor, custom app)       | Requests data or actions from MCP servers          |
| MCP Server     | Exposes APIs or resources in a standardized way                  | Provides access to files, databases, APIs, etc.    |
| Data Sources   | Local or remote resources (databases, files, APIs)               | The actual information or services being accessed  |

MCP typically uses JSON-RPC for communication, with schema-driven data to ensure consistency and reliability.

This architecture allows MCP to standardize and simplify the integration of AI models with diverse external systems, making it scalable and interoperable across applications and platforms[1][3][4].

## Key Components

In the Model Context Protocol (MCP),we have three capabilities that a server can expose features to clients and large language models (LLMs). Here is what each means:

### Tools
- Tools are executable functions or actions that a server exposes, which clients or LLMs can invoke to perform specific tasks or computations.  
- They typically accept structured input arguments and return results after execution.  
- For example, a tool might be a function to calculate the sum of two numbers or fetch weather data for a given city.  
- Tools enable dynamic interaction where the LLM can request the server to perform operations beyond text generation.  
- Implementation involves defining the tool’s name, description, input schema, and the handler logic to process calls and return outputs[2][3].

### Resources
- Resources are data sources or content exposed by the server, accessible via URIs similar to REST API endpoints.  
- They provide textual or binary data that can be read by clients or included as context for LLM interactions.  
- Resources can be static files, logs, documents, or dynamically generated content.  
- Servers can expose lists of resources or templates for resource URIs, and clients can subscribe to updates for frequently changing resources.  
- Resources are application-controlled and validated to ensure security and proper access[3].

### Prompts
- Prompts are predefined, reusable prompt templates and workflows that servers provide for clients and LLMs to standardize common interactions.  
- They are user-controlled, meaning users can explicitly select and use them.  
- Prompts can accept dynamic arguments, include context from resources, chain multiple interaction steps, and guide specific workflows.  
- They can also be surfaced as UI elements like slash commands for easier client integration.  
- Each prompt has a unique name, optional description, and a list of arguments (some required) that customize its behavior.  
- Prompts help structure and automate typical LLM tasks such as generating commit messages or explaining code[1][3].

### Summary Table

| Concept   | Purpose                                  | Key Features                                   | Example Use Case                        |
|-----------|------------------------------------------|-----------------------------------------------|---------------------------------------|
| **Tools**    | Executable functions invoked by clients/LLMs | Accept structured inputs, return outputs      | Calculate sum, fetch weather data     |
| **Resources**| Data/content sources accessible by URI     | Text/binary data, list or template-based URIs | Logs, project files, documents        |
| **Prompts**  | Reusable prompt templates/workflows        | Dynamic arguments, resource context, multi-step | Generate commit message, explain code |

These three capabilities allow MCP servers to offer rich, interactive, and context-aware services to clients and LLMs, facilitating complex workflows and data-driven AI interactions[1][2][3].
