import streamlit as st
class AbrirContaSistemaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    AbrirContaSistemaUI.Inserir()
  def Inserir():
    nome = st.text_input("Informe o nome")
    Data_de_nascimento = st.date_input("Informe a data de nascimento")
    email = st.text_input("Informe o e-mail")
    cpf = st.text_input("infrome o cpf")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      pass
