import streamlit as st
import pandas as pd
from View import view
import time
class ManterBancoUI:
  def main():
    st.header("Controlar Bancos")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterBancoUI.Listar()
    with tab2: ManterBancoUI.Inserir()
    with tab3: ManterBancoUI.Atualizar()
    with tab4: ManterBancoUI.Excluir()    

  def Listar():
    Bancos = view.Banco_Listar()
    if len(Bancos) == 0:
      st.write("Nenhum Banco Cadastrado")
    else:
      dic = []
      for obj in Bancos: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)
  def Inserir():
    nome = st.text_input("Informe o nome")
    endereço = st.text_input("Informe o Endereço")
    if st.button("Inserir"):
      try:
        view.Banco_Inserir(nome,endereço)
        st.success("Banco inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except Exception as erro:
        st.error(erro)
        st.error("Informações invalidas")
  def Atualizar():
    bancos = view.Banco_Listar()
    if len(bancos) == 0:
      st.write("Nenhum banco cadastrado")
    else:
      op = st.selectbox("seleciona banco para atualizar", bancos)
      nome = st.text_input("Informe o nome", op.get_nome())
      endereço = st.text_input("Informe o Endereço", op.get_endereco())
      if st.button("Atualizar"):
        try:
          view.Banco_Atualizar(op.get_id(), nome, endereço)
          st.success("Banco atualizado com sucesso")
          time.sleep(2)
          st.rerun()
        except Exception as erro:
          st.error(erro)
          st.error("Informações invalidas")
  def Excluir():
    bancos = view.Banco_Listar()
    if len(bancos) == 0:
      st.write("Nenhum banco cadastrado")
    else:
      op = st.selectbox("Escolher banco a ser excluido", bancos)
      if st.button("Excluir"):
          id = op.get_id()
          view.Banco_Excluir(id)
          st.success("Banco excluido com sucesso")
          time.sleep(2)
          st.rerun()
