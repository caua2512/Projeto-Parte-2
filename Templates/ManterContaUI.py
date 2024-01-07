import streamlit as st
import pandas as pd
from Models.Conta import Conta,NConta
from View import view
import datetime
import time
class ManterContaUI:
  def main():
    st.header("Controlar Contas")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterContaUI.Listar()
    with tab2: ManterContaUI.Inserir()
    with tab3: ManterContaUI.Atualizar()
    with tab4: ManterContaUI.Excluir()    

  def Listar():
    Contas = view.Conta_Listar()
    if len(Contas) == 0:
      st.write("Nenhuma Conta Cadastrada")
    else:
      dic = []
      for obj in Contas: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)
  def Inserir():
    clientes = view.Cliente_Listar()
    cliente = st.selectbox("Selecione o cliente", clientes)
    Data_De_Abertura = datetime.datetime.now()
    NumeroB = st.text_input("Informe o numero do banco")
    
    Saldo = st.number_input("Informe o Saldo Inical")
    if st.button("Inserir"):
      try:
        view.Conta_Inserir(cliente.get_id(), Data_De_Abertura, NumeroB, Saldo)
        st.success("Conta inserida com sucesso")
        time.sleep(2)
        st.rerun()
      except Exception as erro:
        st.error(erro)
        st.error("Informações invalidas")
  def Atualizar():
    contas = view.Conta_Listar()
    if len(contas) == 0:
      st.write("Nenhuma conta cadastrada")
    else:
      op = st.selectbox("Escolhar a Conta para atualizar", contas)
      Data_De_Abertura = st.text_input("Escolhar uma nova data")
      clientes = view.Cliente_Listar()
      cliente_atual = view.Cliente_Listar_Id((op.get_id_Cliente()))
      if cliente_atual is not None:
        cliente = st.selectbox("Selecione o novo cliente", clientes, clientes.index(cliente_atual))
      else:
        cliente = st.selectbox("Selecione o novo cliente", clientes)
      NumeroB = st.text_input("Informe o numero do banco", op.get_Numero_Do_Banco())
      Saldo = st.number_input("Informe o Saldo Inical", op.get_saldo())
      if st.button("Atualizar"):
        try:
          data = datetime.datetime.strptime(Data_De_Abertura,"%d/%m/%Y %H:%M")
          view.Conta_Atualizar(op.get_id(),cliente.get_id(),data, NumeroB, Saldo)
          st.success("Conta atualizada com sucesso")
          time.sleep(2)
          st.rerun()
        except Exception as erro:
          st.error(erro)
          st.error("Informações invalidas")
  def Excluir():
    contas = view.Conta_Listar()
    if len(contas) == 0:
      st.write("Nenhuma Conta Cadastrada")
    else:
      op = st.selectbox("Exclusão de Conta", contas)
      if st.button("Excluir"):
        view.Conta_Excluir(op.get_id())
        st.success("Conta excluida com sucesso")
        time.sleep(2)
        st.rerun()
