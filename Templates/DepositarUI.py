import streamlit as st
from View import view
import time
class DepositarUI:
  def main():
    st.header("Depositar")
    DepositarUI.Depositar()
  def Depositar():
    contas = view.Conta_Listar()
    conta = st.selectbox("seleciona Conta para depositar", contas)
    saldo = st.number_input("Saldo do saque")
    if st.button("Depositar"):
      view.depositar(conta.get_id(),saldo)
      st.success("Deposito realizado com sucesso")
      time.sleep(2)
      st.rerun()
        
