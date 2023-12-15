import streamlit as st
import pandas as pd
import numpy as np
import time
st.set_page_config('ANAPH', page_icon='⚡')

def dialog_botao_fechar():
    st.write("###  Resultado do PopUp fechado:")
    st.write("#### Nada à salvar!")
    popup.close()

popup = st.dialog(
    "primeiro_popup", title="Crie sua conta1",
    on_botao_fechar_clicked=dialog_botao_fechar, pode_fechar=True)

def dialog_botao_criar():
    st.write("### Resultado do Criar no PopUp:")
    st.write(f"#### Eai {st.session_state.usuario})
    st.write(f"#### Conta Criada")
    popup.close()


with popup:
    usu = st.text_input("Usuário", key="usuario")
    pas = st.text_input("Senha", key="senha")
    pas1 = st.text_input("Confirme sua senha", key= "confirme")
    if pas1 != pas:
      st.caption(':red[Senha não confere]')
    st.checkbox("Eu aceito cookies!", key="cookies")
    st.form_submit_button("Criar", on_click=dialog_botao_criar)


if st.button("Open dialog", key="first_dialog_button"):
    dialog.open()

st.header('ANAPH', divider='rainbow')
st.image('https://i.imgur.com/1P4Ggm3.png',width=700)
st.write('Analisamos o seu consumo de energia elétrica!')

#Explicação
st.title('Como funciona?')
st.write(' **Aqui no site da ANAPH é mais fácil calcular o seu consumo de energia, podendo filtrar na data desejada, quando e onde quiser! Crie sua conta no menu CADASTRO para ter acesso completo às funcionalidades do site. Agradecemos a sua visita.** ')
