from dotenv import load_dotenv
import streamlit as st
from crewai import Agent, Crew, Process, Task, LLM
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

load_dotenv()

file1 = PDFKnowledgeSource(file_paths=["7950_PDF.pdf"])

llm = LLM(
    model="openai/gpt-4o-mini",
    temperature=0,
    max_tokens=1024,
)

agent = Agent(
    name="PostgreSQL Assistante",
    description="Responde perguntas sobre PostgreSQL",
    role="PostgreSQL Expert",
    goal="Responde perguntas sobre o PostgreSQL",
    backstory="Você é um assistente especializado em responder perguntas sobre o PostgreSQL.",
    tools=[],
    verbose=True,
    llm=llm,
)

task = Task(
    description="Responda a seguinte pergunta: {question}",
    expected_output="Uma resposta concisa e precisa.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,  # or Process.parallel if you want parallel execution
    verbose=True,
    knowledge_sources=[file1],
)

st.title("🔎 PostgreSQL AI Assistante")
st.write("Esse assistente AI ajuda você com **PostgreSQL**.")

with st.sidebar:
    user_input = st.text_area("Faça uma pergunta sobre PostgreSQL:")

if st.button("Enviar 🚀"):
    if not user_input.strip():
        st.warning("⚠️ Por favor, insira sua pergunta antes de enviar.")
    else:
        st.write("⏳ Processando sua requisição... Aguarde.")
        result = crew.kickoff(inputs={"question": user_input})

        st.subheader("✅ PostgreSQL AI Response:")
        st.write(result)
