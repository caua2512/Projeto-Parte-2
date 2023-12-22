import streamlit as st
class ManterClienteUI:
  def main():
    st.header("Controlar Cliente")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterClienteUI.Listar()
    with tab2: ManterClienteUI.Inserir()
    with tab3: ManterClienteUI.Atualizar()
    with tab4: ManterClienteUI.Excluir()    

  def Listar():
    pass
  def Inserir():
    nome = st.text_input("Informe o nome")
    Data_de_nascimento = st.date_input("Informe a data de nascimento")
    email = st.text_input("Informe o e-mail")
    cpf = st.text_input("infrome o cpf")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      pass
  def Atualizar():
    nome = st.text_input("Informe o nome")
    Data_de_nascimento = st.date_input("Informe a data de nascimento")
    email = st.text_input("Informe o e-mail")
    cpf = st.text_input("infrome o cpf")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Atualizar"):
      pass
  def Excluir():
    pass
