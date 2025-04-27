"""
https://www.datacamp.com/tutorial/openai-agents-sdk-tutorial
"""

from dotenv import load_dotenv
from openai import OpenAI
from agents import Runner, WebSearchTool, FileSearchTool, Agent, ModelSettings
import asyncio
import sys
import os
import streamlit as st


load_dotenv()

client = OpenAI()

VECTOR_STORE_NAME = "ConstruSummit Arquivos"

vector_store = [ v for v in client.vector_stores.list() if v.name == VECTOR_STORE_NAME ]
if not vector_store:
    vector_store = client.vector_stores.create(name=VECTOR_STORE_NAME)
    print(f"Vector Store ID: {vector_store.id}")
    vector_store_id = vector_store.id

    file1 = client.files.create(
        file=open("knowledge/ConstruSummit.pdf", "rb"),
        purpose="assistants"
    )

    file_ids = [
        file1.id
    ]
    
    client.vector_stores.file_batches.create(
        vector_store_id=vector_store.id,
        file_ids=file_ids   
    )
else:
    vector_store_id = vector_store[0].id

agent = Agent(
    name="ConstruSummit Assistente",
    instructions="Você é um assistente especializado em responder perguntas sobre o ConstruSummit.",
    model="gpt-4o",
    model_settings=ModelSettings(
        temperature=0.7,
        max_tokens=1024,
    ),
    tools=[
        FileSearchTool(
            vector_store_ids=[vector_store_id],
            max_num_results=3
        ),
        WebSearchTool(
            user_location={
                "type": "approximate",
                "country": "BR",
                "city": "Florianópolis"
            },
            search_context_size="low"
        )
    ]
)

def streamlit_main():
    st.set_page_config(page_title="ConstruSummit Q&A", page_icon="🏗️", layout="centered")
    st.image("https://sienge.com.br/wp-content/themes/reactphp-03-02-2025/assets/images/construsummit/logo-horizontal-colorido-laranja.svg", width=250)
    st.title("ConstruSummit AI Assistant")
    st.write("Faça perguntas sobre o evento ConstruSummit e receba respostas instantâneas!")
    
    with st.sidebar:
        st.header("Sobre o Evento")
        st.write("[Site Oficial](https://sienge.com.br/construsummit/)")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Digite sua pergunta sobre o ConstruSummit..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("⏳ Pensando...")
            
            try:
                result = asyncio.run(Runner.run(agent, prompt))
                response = result.final_output
                message_placeholder.markdown(response)
                
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                message_placeholder.markdown(f"❌ Erro ao processar sua pergunta: {str(e)}")

if __name__ == "__main__":
    streamlit_main()
    