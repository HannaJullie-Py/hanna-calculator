import streamlit as st
import pandas as pd
import numpy as np
import time

usu = st.text_input('Crie seu nome de usuário')
pas = st.text_input('Crie sua senha')

butao = st.button('Enter em cada uma das caixas para criar')

if butao:
  st.write('Conta criada :D')

