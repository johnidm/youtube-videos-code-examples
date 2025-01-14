import streamlit as st

from services import (
    get_assistant_id,
    get_history_messages,
    get_thread_id,
    get_chat_response,
    Message,
    USER,
    ASSISTANT,
)

st.set_page_config(page_title="OpenAI Chat", page_icon=":tomato:")
st.title("🗨️ AI Chat")

st.markdown(
    r"""
    <style>
    .stDeployButton {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


if "is_thread_id" not in st.session_state:
    st.session_state.is_thread_id = False


def set_is_thread_id():
    st.session_state.is_thread_id = True


with st.form(key="thread"):
    assistent_input = st.text_input(
        label="Informa o assistent da conversa",
        value="PostgreSQL Expert",
    )
    thread_input = st.text_input(
        label="Informa o código da conversa",
    )
    submit_button = st.form_submit_button(
        label="Inicar Chat",
        on_click=set_is_thread_id,
    )


if st.session_state.is_thread_id:
    assistant_id = get_assistant_id(assistent_input)

    if not thread_input:
        thread = get_thread_id()
        thread_id = thread.id

        st.session_state.messages = []
    else:
        thread_id = thread_input

    st.caption(f"Thread ID: {thread_id} - Assitent ID: {assistant_id}")

    if "messages" not in st.session_state:
        messages_history = get_history_messages(thread_id)
        if messages_history:
            st.session_state.messages = messages_history
        else:
            st.session_state.messages = []

    st.subheader("Mensagens antigas:")

    if st.session_state.messages:
        for message in st.session_state.messages:
            st.chat_message(message.actor).write(message.payload)
    else:
        st.write("Nenhuma mensagem")

    st.markdown("""---""")
    welcome = Message(actor=ASSISTANT, payload="Olá, como eu posso ajudar você?")
    st.chat_message(welcome.actor).write(welcome.payload)

    if prompt := st.chat_input("Digite a sua pergunta"):
        assistant_chat = Message(
            actor=USER,
            payload=prompt,
        )

        st.session_state["messages"].append(assistant_chat)
        st.chat_message(assistant_chat.actor).write(assistant_chat.payload)

        with st.spinner("Gerando a resposta..."):
            response: str = get_chat_response(
                assistant_id,
                thread_id,
                prompt,
            )

            assistant_chat = Message(actor=ASSISTANT, payload=response)

            st.session_state["messages"].append(
                Message(
                    actor=assistant_chat.actor,
                    payload=assistant_chat.payload,
                )
            )
            st.chat_message(assistant_chat.actor).write(assistant_chat.payload)
