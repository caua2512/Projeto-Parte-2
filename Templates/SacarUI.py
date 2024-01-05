import streamlit as st
from View import view
import time
class SacarUI:
  def main():
    st.header("Sacar")
    SacarUI.Sacar()
  def Sacar():
    contas = view.Conta_Listar()
    conta = st.selectbox("seleciona Conta para sacar", contas)
    saldo = st.number_input("Saldo do saque")
    if st.button("Sacar"):
      view.sacar(conta.get_id(),saldo)
      st.success("Saque realizado com sucesso")
      time.sleep(2)
      st.rerun()
      
