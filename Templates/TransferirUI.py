import streamlit as st
from View import view
import time
class TransferirUI:
  def main():
    st.header("Transferencia")
    TransferirUI.transferir()
  def transferir():
    id_logado = st.session_state["cliente_id"]
    contas1 = view.listar_contas_do_cliente(id_logado)
    conta1 = st.selectbox("seleciona conta da transferencia", contas1)
    contas2 = view.Conta_Listar()
    conta2 = st.selectbox("seleciona conta para depositar", contas2)
    saldo = st.number_input("Saldo Da Transferencia")
    if st.button("Transferir"):
      try:
        view.transferir(conta1.get_id(),conta2.get_id(),saldo)
        st.success("Transferencia realizado com sucesso")
        time.sleep(2)
        st.rerun()
      except:
        st.error("Informações invalidas")
