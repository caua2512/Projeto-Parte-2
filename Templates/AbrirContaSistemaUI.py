import streamlit as st
from View import view
import datetime
import time
class AbrirContaSistemaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    AbrirContaSistemaUI.Inserir()
  def Inserir():
    bancos = view.Banco_Listar()
    banco = st.selectbox("selecione o Banco",  bancos)
    nome = st.text_input("Informe o nome")
    Data_de_nascimento = st.text_input("Informe a data de nascimento")
    email = st.text_input("Informe o e-mail")
    cpf = st.text_input("infrome o cpf")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Cadastra-se"):
      Data = datetime.datetime.strptime(Data_de_nascimento,"%d/%m/%Y %H:%M")
      try:
        view.Cliente_Inserir(banco.get_id(),nome ,Data, email, cpf, fone, senha)
        st.sucess("Cadastrado realizado com sucesso")
        time.sleep(2)
        st.rerun()
      except:
        st.error("Dado(s) invalido(s)")
