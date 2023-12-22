import streamlit as st
class SacarUI:
  def main():
    st.header("Sacar")
    SacarUI.Sacar()
  def Sacar():
    saldo = st.number_input("Saldo do saque")
    if st.button("Sacar"):
      pass
