import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
@st.cache_data
def load_data():
    return pd.read_csv("clientes.csv")  # Certifique-se de que o arquivo está no diretório correto

df = load_data()

# Título do aplicativo
st.title("Dashboard de Clientes")

# Selecionar variável para gráfico
variavel = st.selectbox("Selecione a variável categórica para visualizar:", 
                        ["sexo", "estado_civil", "dependentes", "educacao", "empregado", "imovel", "aprovacao_emprestimo"])

# Criar gráfico de pizza
fig = px.pie(df, names=variavel, title=f"Distribuição de {variavel}")

# Exibir gráfico
st.plotly_chart(fig)
