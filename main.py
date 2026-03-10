#titulo
# input do chat (campo mensagem)
    # mostrar a mensagem que o user enviou no chat
    # pegar a pergunta e enviar para uma IA responder
    # exibir a resposta da IA na tela

#Streamlit -> py no front e backend
# Ia utilizada: OpenAI (ChatGPT)
# pip install streamlit openai

#python -m streamlit run main.py 

import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

modelo_ia = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.write("### ChatBot com IA") 

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    resposta_modelo = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o-mini"
    )
    
    resposta_ia = resposta_modelo.choices[0].message.content

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
