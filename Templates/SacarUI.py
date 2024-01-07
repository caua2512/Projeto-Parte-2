import streamlit as st
from View import view
import time
class SacarUI:
  def main():
    st.header("Sacar")
    SacarUI.Sacar()
  def Sacar():
    id_logado = st.session_state["cliente_id"]
    contas = view.listar_contas_do_cliente(id_logado)
    conta = st.selectbox("seleciona Conta para sacar", contas)
    saldo = st.number_input("Saldo do saque")
    if st.button("Sacar"):
      try:
        view.sacar(conta.get_id(),saldo)
        st.success("Saque realizado com sucesso")
        time.sleep(2)
        st.rerun()
      except:
        st.error("Informações invalidas")
      
