import streamlit as st
class TransferirUI:
  def main():
    st.header("Transferencia")
    TransferirUI.transferir()
  def transferir():
    saldo = st.number_input("Saldo Da Transferencia")
    if st.button("Transferir"):
      pass
