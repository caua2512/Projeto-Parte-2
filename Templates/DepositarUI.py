import streamlit as st
from View import view
import time
class DepositarUI:
  def main():
    st.header("Depositar")
    DepositarUI.Depositar()
  def Depositar():
    id_logado = st.session_state["cliente_id"]
    contas = view.listar_contas_do_cliente(id_logado)
    conta = st.selectbox("seleciona Conta para depositar", contas)
    saldo = st.number_input("Saldo do saque")
    if st.button("Depositar"):
      try:
        view.depositar(conta.get_id(),saldo)
        st.success("Deposito realizado com sucesso")
        time.sleep(2)
        st.rerun()
      except:
        st.error("Informações invalidas")
