import streamlit as st
import pandas as pd
import numpy as np
import time


#Título
st.set_page_config(page_title="ANAPH",page_icon="💡")
st.sidebar.header("ANAPH")
st.sidebar.image('https://i.imgur.com/1P4Ggm3.png', width=70)
st.header('ANAPH', divider='rainbow')
st.image('https://i.imgur.com/1P4Ggm3.png',width=700)
st.write('Analisamos o seu consumo de energia elétrica!')

#Explicação
st.title('Como funciona?')
st.write(' **Aqui no site da ANAPH é mais fácil calcular o seu consumo de energia, podendo filtrar na data desejada, quando e onde quiser! Crie sua conta no menu CADASTRO para ter acesso completo às funcionalidades do site. Agradecemos a sua visita.** ')
