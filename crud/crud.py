from os import write
from numpy.core.fromnumeric import size
import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import pandas as pd



st.sidebar.title("Menu")
Page_cliente = st.sidebar.selectbox("Cliente", ["Incluir", "Alterar", "Excluir", "Consultar"])

if Page_cliente == 'Consultar':
    st.title("Clientes")
    costumerList = []

    for item in ClienteController.SelecionarTodos():
        costumerList.append([item.patrimonio, item.renda, item.profissao, item.objetivo])

    df = pd.DataFrame(
        costumerList,
        columns=['Patrimonio', 'Renda', 'Profissao', 'Objetivo']
    )

    st.table(df)

if Page_cliente == 'Incluir':
    st.title("Incluir Dados")
    with st.form(key="include_cliente"):
        input_patrimonio = st.number_input(label="Insira o seu patrimonio", format="%d", step=10)
        input_renda = st.number_input(label="Insira sua renda: ", format="%d", step=10)
        input_profissao = st.text_input(label="Insira sua profissão")
        input_objetivo = st.selectbox("Selecione seu objetivo", ["Aposentadoria", "Renda Extra", "Futuro Seguro", "Investimento", "Imoveis"])
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:

        ClienteController.Incluir(cliente.Cliente(0, input_patrimonio, input_renda, input_profissao, input_objetivo))
        st.success("Cliente incluido com sucesso!")








