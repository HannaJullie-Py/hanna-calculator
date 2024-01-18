import streamlit as st
import pandas as pd
import numpy as np
import time
st.set_page_config('ANAPH', page_icon='⚡')
st.header('ANAPH', divider='rainbow')
st.image('https://i.imgur.com/1P4Ggm3.png',width=700)
st.write('Analisamos o seu consumo de energia elétrica!')

page_bg_img = '''
<style>
body {
background-image: url("https://static.mundoeducacao.uol.com.br/mundoeducacao/2023/06/barragem-de-uma-usina-hidreletrica.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

#Explicação
st.title('Como funciona?')
st.write(' **Aqui no site da ANAPH é mais fácil calcular o seu consumo de energia, podendo filtrar na data desejada, quando e onde quiser! Crie sua conta no menu CADASTRO para ter acesso completo às funcionalidades do site. Agradecemos a sua visita.** ')
