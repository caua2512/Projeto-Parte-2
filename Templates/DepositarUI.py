import streamlit as st
class DepositarUI:
  def main():
    st.header("Depositar")
    DepositarUI.Depositar()
  def Depositar():
    saldo = st.number_input("Saldo do deposito")
    if st.button("Depositar"):
      pass
