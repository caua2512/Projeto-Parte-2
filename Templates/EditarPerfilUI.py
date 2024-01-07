import streamlit as st
from View import view
import datetime
import time
class EditarPerfilUI:
  def main():
    st.header("Editar Perfil")
    EditarPerfilUI.Editar()
  def Editar():
    clientes = view.Cliente_Listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      if st.session_state["cliente_nome"] == "admin":
        id = st.session_state["cliente_id"]
        bancos = view.Banco_Listar()
        banco = st.selectbox("Selecione o novo Banco", bancos)
        Nome = "admin"
        Data_de_nascimento = st.text_input("Informe a data de nascimento em formato dd/mm/YYYY")
        email = st.text_input("Informe o e-mail")
        cpf = st.text_input("infrome o cpf")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha")
        if st.button("Editar"):
          try:
            data = datetime.datetime.strptime(Data_de_nascimento, '%d/%m/%Y %H:%M')
            view.Cliente_Editar_Perfil(id,banco.get_id(), Nome, data, email, cpf, fone, senha)
            st.success("Perfil Atualizado")
            time.sleep(2)
            st.rerun()
          except:
            st.error("Informações invalidas")
      else:
        id = st.session_state["cliente_id"]
        bancos = view.Banco_Listar()
        banco = st.selectbox("Selecione o novo Banco", bancos)
        nome = st.text_input("Informe o nome")
        Data_de_nascimento = st.text_input("Informe a data de nascimento em formato dd/mm/YYYY")
        email = st.text_input("Informe o e-mail")
        cpf = st.text_input("infrome o cpf")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha")
        if st.button("Editar"):
          try:
            data = datetime.datetime.strptime(Data_de_nascimento, '%d/%m/%Y %H:%M')
            view.Cliente_Editar_Perfil(id,banco.get_id(), nome, data, email, cpf, fone, senha)
            st.success("Perfil Atualizado")
            time.sleep(2)
            st.rerun()
          except:
            st.error("Informações invalidas")
