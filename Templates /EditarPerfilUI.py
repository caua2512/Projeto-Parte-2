import streamlit as st
class EditarPerfilUI:
  def main():
    st.header("Controlar Cliente")
    EditarPerfilUI.Editar()
  def Editar():
    nome = st.text_input("Informe o nome")
    Data_de_nascimento = st.date_input("Informe a data de nascimento")
    email = st.text_input("Informe o e-mail")
    cpf = st.text_input("infrome o cpf")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Atualizar"):
      pass
