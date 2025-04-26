from crewai import Agent, Task, Crew, Process
from crewai_tools import WebsiteSearchTool, PDFSearchTool
from dotenv import load_dotenv

load_dotenv()
pdf_tool = PDFSearchTool(pdf_path="7950_PDF.pdf")
website_tool = WebsiteSearchTool(
    website="https://sienge.com.br/",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
)

agent = Agent(
    role="Um assistente que responde perguntas sobre o `Construsummit 2025",
    goal="Responde perguntas sobre o Construsummit 2025",
    backstory="Background information about your agent",
    tools=[pdf_tool, website_tool],
    name="Construsummit 2025 Assistant",
    description="Answers questions using a website"
)

task = Task(
    description="Answer the following question using the provided sources: {question}",
    expected_output="A concise, accurate answer.",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,  # or Process.parallel if you want parallel execution
    verbose=True,
    llm="gpt-4o"
)


def main():
    while (question := str(input("Pergunta (ENTER para sair): ")).strip()) != "":
        result = crew.kickoff(inputs={"question": question})
        print(result)

if __name__ == "__main__":
    main()