from dotenv import load_dotenv
import streamlit as st
from crewai import Agent, Crew, Process, Task, LLM
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

load_dotenv()

file1 = PDFKnowledgeSource(file_paths=["ConstruSummit.pdf"])

llm = LLM(
    model="openai/gpt-4o-mini",
    temperature=0,
    max_tokens=1024,
)

agent = Agent(
    name="ConstruSummit Assistente",
    description="Responde perguntas sobre ConstruSummit",
    role="ConstruSummit Expert",
    goal="Responde perguntas sobre o ConstruSummit",
    backstory="Você é um assistente especializado em responder perguntas sobre o ConstruSummit.",
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

st.title("🔎 ConstruSummit AI Assistente")
st.write("Esse assistente AI ajuda você com **ConstruSummit**.")

with st.sidebar:
    user_input = st.text_area("Faça uma pergunta sobre ConstruSummit:")

if st.button("Enviar 🚀"):
    if not user_input.strip():
        st.warning("⚠️ Por favor, insira sua pergunta antes de enviar.")
    else:
        st.write("⏳ Processando sua requisição... Aguarde.")

        response = crew.kickoff(inputs={"question": user_input})
        result = response.raw
        st.subheader("✅ ConstruSummit AI Response:")
        st.write(result)
        st.text_area("Token Usage:", response.token_usage)