import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Cadastro",page_icon="📄")
st.title('Cadastro')

st.divider()

usu = st.text_input('Crie seu nome de usuário')
pas = st.text_input('Crie sua senha')
pas1 = st.text_input('Confirme sua senha')


butao = st.button('Enter')
if pas1 != pas:
  st.caption(':red[Senha não confere]')

if butao:
  st.caption(':green[Conta criada :D]')

st.divider()

