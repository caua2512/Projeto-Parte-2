import streamlit as st
from View import view
import time
class TransferirUI:
  def main():
    st.header("Transferencia")
    TransferirUI.transferir()
  def transferir():
    contas = view.Conta_Listar()
    conta1 = st.selectbox("seleciona conta da transferencia", contas)
    conta2 = st.selectbox("seleciona conta para depositar", contas)
    saldo = st.number_input("Saldo Da Transferencia")
    if st.button("Transferir"):
      view.transferir(conta1.get_id(),conta2.get_id(),saldo)
      st.success("Saque realizado com sucesso")
      time.sleep(2)
      st.rerun()
