import streamlit as st
class AbrirContaUI:
  def main():
    st.header("Abrir Conta")
    AbrirContaUI.Inserir()
  def Inserir():
    DataDeAbertura = st.date_input("Informe o nome")
    Saldo = st.number_input("Informe o Saldo atual")
    if st.button("Inserir"):
      pass
