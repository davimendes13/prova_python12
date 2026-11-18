import pandas as pd
import streamlit as st


df = pd.read_excel("saeb_aprendizado_territorios-7-2023-EM.xlsx",
sheet_name="estados", engine="openpyxl")


st.set_page_config(page_title="Aprendizado estados", layout="wide")

st.title("Aprendizado em UFs")

colunas = [
    "uf", "lingua portuguesa insuficiente", "matematica insuficiente"
]
     
df_filtrado = df [
    (df["uf"].isin(["MG", "BA", "CE", "PR"]))
]

st.dataframe(df_filtrado, column_order=colunas)