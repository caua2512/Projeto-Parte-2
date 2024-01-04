import streamlit as st
import pandas as pd
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
    Contas = view.Contas_Listar()
    if len(Contas) == 0:
      st.write("Nenhuma Conta Cadastrada")
    else:
      dic = []
      for obj in Contas:
        for Conta in Contas:
          id = Conta.get_id()
          id_Cliente = Conta.get_id_Cliente()
          Data_De_Abertura = Conta.get_Data_De_Abertura()
          Numero_Do_Banco = Conta.Get_Numero_Do_Banco()
          Saldo = Conta.get_saldo()
          dic.append(obj[id, id_Cliente,Data_De_Abertura,Numero_Do_Banco,Saldo])
        
      df = pd.DataFrame(dic, columns=["id", "ID do Cliente", "Data de abertura", "Numero do banco", "Saldo"])
      st.dataframe(df)

  def Inserir():
    Data_De_Abertura = st.text_input("Informe a data de Abertura em formato: dd/mm/aaaa HH:MM *")
    clientes = view.Cliente_Listar()
    cliente = st.selectbox("Selecione o cliente", clientes)
    NumeroB = st.text_input("Informe o numero do banco")
    Saldo = st.number_input("Informe o Saldo Inical")
    if st.button("Inserir"):
        data = datetime.datetime.strptime(Data_De_Abertura, "%d/%m%/%Y %H:%M")
        view.Conta_Inserir(cliente.get_id(), data, NumeroB, Saldo)
        st.sucess("Conta Inserida com sucesso")
        time.sleep(2)
        st.rerun()
  def Atualizar():
    contas = view.Conta_Listar()
    if len(contas) == 0:
      st.write("Nenhuma conta cadastrada")
    else:
      op = st.selectbox("Escolhar a Conta para atualizar", contas)
      Data_De_Abertura = st.text_input("Informe a data de Abertura em formato: dd/mm/aaaa HH:MM *", op.get_Data_De_Abertura().strftime('%d/%m/%Y %H:%M'))
      NumeroB = st.text_input("Informe o numero do banco", op.Get_Numero_Do_Banco())
      Saldo = st.number_input("Informe o Saldo Inical", op.get_saldo())
      clientes = view.Cliente_Listar
      cliente_atual = view.Cliente_Listar_Id((op.get_id_Cliente()))
      if cliente_atual is not None:
        cliente = st.selectbox("Selecione o novo cliente", clientes, clientes.index(cliente_atual))
      else:
        cliente = st.selectbox("Selecione o novo cliente", clientes)
      if st.button("Atualizar"):
        try:
          data = datetime.datetime.strptime(Data_De_Abertura,"%d/%m/%Y %H:%M")
          view.Conta_Atualizar(op.get_id(), cliente.get_id(), data, NumeroB, Saldo)
          time.sleep(2)
          st.rerun()
        except:
          st.error("Informações invalidas")
  def Excluir():
    contas = view.Conta_Listar()
    if len(contas) == 0:
      st.write("Nenhuma Conta Cadastrada")
    else:
      op = st.selectbox("Exclusão de Conta", contas)
      if st.button("Excluir"):
        view.Conta_Excluir(op.get_id())
        st.sucess("Conta excluida com sucesso")
        time.sleep(2)
        st.rerun()
