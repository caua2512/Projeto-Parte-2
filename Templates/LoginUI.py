import streamlit as st
from View import view
import time
class loginUI:
  def main():
    st.header("Login")
    loginUI.Entrar()
  def Entrar():
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Entrar"):
      cliente = view.Cliente_Login(email,senha)
      if cliente is not None:
        st.success("Login realizado com sucesso")
        st.success("Bem-vindo(a)," + cliente.get_Nome())
        st.session_state["cliente_id"] = cliente.get_id()
        st.session_state["cliente_nome"] = cliente.get_Nome()
      else:
        st.error("Usuario ou senha invalido(s)")
      time.sleep(2)
      st.rerun()
