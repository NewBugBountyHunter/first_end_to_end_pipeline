import streamlit as st
import pandas as pd
import plotly.express as px
import os

def load_data():
    try:
        df = pd.read_parquet(os.path.join('data','gold','vendas_v1_final.parquet'))
        return df
    
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return pd.DataFrame()

df = (load_data())

if df is not None:

    st.sidebar.title("Dashboard de vendas")
    st.sidebar.header("Filtros")

    categorias_selecionadas = st.sidebar.multiselect(
        "Selecione as categorias",
        options=df['categoria'].unique(),
        default=df['categoria'].unique()
    )

    df_filtrado = df[df['categoria'].isin(categorias_selecionadas)]

c1,c2,c3,c4 =st.columns(4)

with c1:
    st.metric("Total_Vendas", f"R$ {df_filtrado['total_vendas_categoria'].sum():,.2f}")
    
with c2:
    total_transaçoes = int(df_filtrado['quantidade_transacoes'].sum())
    st.metric("Total_transaçoes", f"{total_transaçoes:,d}")

with c3:
    st.metric("Ticket_Médio", f"R$ {df_filtrado['ticket_medio'].mean():,.2f}")

with c4:
    st.metric("Categorias", f"{df_filtrado['categoria'].nunique()}")

if not df_filtrado.empty:
    fig=px.bar(
        df_filtrado,
        x='categoria',
        y='total_vendas_categoria',
        title='Total de vendas por Categoria',
        labels={'total_vendas_categoria': 'Total de Vendas (R$)', 'categoria' : 'Categoria'},
        text_auto='.2s'
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Selecione pelo menos uma categoria para visualizar o gráfico.")
