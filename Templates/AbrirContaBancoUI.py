import streamlit as st
from View import view
import datetime
import time
class AbrirContaUI:
  def main():
    st.header("Abrir Conta")
    AbrirContaUI.Inserir()
  def Inserir():
    id = st.session_state["cliente_id"]
    DataDeAbertura = datetime.datetime.now()
    NumeroDoBanco = st.text_input("Numero do Banco")
    Saldo = st.number_input("Informe o Saldo atual")
    if st.button("Abrir Conta"):
      try:
        view.Conta_Inserir(id, DataDeAbertura, NumeroDoBanco, Saldo)
        st.success("Conta Aberta com sucesso")
        time.sleep(2)
        st.rerun()
      except:
        st.error("Informações invalidadas")
