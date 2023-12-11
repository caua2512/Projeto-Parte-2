import streamlit as st
class loginUI:
  def main():
    st.header("Login")
    loginUI.Entrar()
  def Entrar():
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Entrar"):
      pass
