import streamlit as st
import pandas as pd
from View import view
import datetime
import time
class ManterTransferenciaUI:
  def main():
    st.header("Controlar Transferencias")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterTransferenciaUI.Listar()
    with tab2: ManterTransferenciaUI.Inserir()
    with tab3: ManterTransferenciaUI.Atualizar()
    with tab4: ManterTransferenciaUI.Excluir()    

  def Listar():
    Transferencias = view.Transferencia_Listar()
    if len(Transferencias) == 0:
      st.write("Nenhuma Conta Cadastrada")
    else:
      dic = []
      for obj in Transferencias:
        for Transferencia in Transferencias:
          id = Transferencia.get_id()
          id_Cliente = Transferencia.get_id_Cliente()
          id_Conta1 = Transferencia.get_id_Conta1()
          id_Conta2 = Transferencia.get_id_Conta2()
          Data_De_Transferencia = Transferencia.get_Data_De_Transferencia()
          Saldo_Da_Transferencia = Transferencia.get_Saldo_da_transferencia()
          dic.append(obj[id, id_Cliente,id_Conta1,id_Conta2,Data_De_Transferencia, Saldo_Da_Transferencia])
        
      df = pd.DataFrame(dic, columns=["id", "ID do Cliente", "Conta1", "Conta2", "Data da Transferencia","Saldo da transferencia"])
      st.dataframe(df)

  def Inserir():
    Data_De_Transferencia = st.text_input("Informe a data da Transferencia em formato: dd/mm/aaaa HH:MM *")
    clientes = view.Cliente_Listar()
    cliente = st.selectbox("Selecione o cliente", clientes)
    contas1 = view.Conta_Listar()
    conta1 = st.selectbox("Selecione o cliente", contas1)
    contas2 = view.Conta_Listar()
    conta2 = st.selectbox("Selecione o cliente", contas2)
    Saldo_Da_Transferencia = st.number_input("Informe o Saldo Da tranferencia")
    if st.button("Inserir"):
        data = datetime.datetime.strptime(Data_De_Transferencia, "%d/%m%/%Y %H:%M")
        view.Transferencia_Inserir(cliente.get_id(),conta1.get_id(),conta2.get_id(), data, Saldo_Da_Transferencia)
        st.sucess("Transferencia Inserida com sucesso")
        time.sleep(2)
        st.rerun()
  def Atualizar():
    transferencias = view.Transferencia_Listar()
    if len(transferencias) == 0:
      st.write("Nenhuma transferencia cadastrada")
    else:
      op = st.selectbox("Escolhar a Conta para atualizar", transferencias)
      Data_De_Transferencia = st.text_input("Informe a data de Transferencia em formato: dd/mm/aaaa HH:MM *", op.get_Data_De_Transferencia().strftime('%d/%m/%Y %H:%M'))
      Saldo_Da_Transferencia = st.number_input("Informe o Saldo Inical", op.get_Saldo_da_transferencia())
      clientes = view.Cliente_Listar()
      cliente_atual = view.Cliente_Listar_Id((op.get_id_Cliente()))
      if cliente_atual is not None:
        cliente = st.selectbox("Selecione o novo cliente", clientes, clientes.index(cliente_atual))
      else:
        cliente = st.selectbox("Selecione o novo cliente", clientes)
      contas1 = view.Conta_Listar()
      conta1_atual = view.Conta_Listar_Id((op.get_id_Conta1()))
      if conta1_atual is not None:
        conta1 = st.selectbox("Selecione o novo cliente", contas1, contas1.index(conta1_atual))
      else:
        conta1 = st.selectbox("Selecione o novo cliente", contas1)
      contas2 = view.Conta_Listar()
      conta2_atual = view.Conta_Listar_Id((op.get_id_Cliente()))
      if conta2_atual is not None:
        conta2 = st.selectbox("Selecione o novo cliente", contas2, contas2.index(conta2_atual))
      else:
        conta2 = st.selectbox("Selecione o novo cliente", contas2)
      if st.button("Atualizar"):
        try:
          data = datetime.datetime.strptime(Data_De_Transferencia,"%d/%m/%Y %H:%M")
          view.Transferencia_Atualizar(op.get_id(), cliente.get_id(),conta1.get_id(),conta2.get_id(), data, Saldo_Da_Transferencia)
          time.sleep(2)
          st.rerun()
        except:
          st.error("Informações invalidas")
  def Excluir():
    Transferencias = view.Transferencia_Listar()
    if len(Transferencias) == 0:
      st.write("Nenhuma Conta Cadastrada")
    else:
      op = st.selectbox("Exclusão de Transferencia", Transferencias)
      if st.button("Excluir"):
        view.Transferencia_Excluir(op.get_id())
        st.sucess("Conta excluida com sucesso")
        time.sleep(2)
        st.rerun()
