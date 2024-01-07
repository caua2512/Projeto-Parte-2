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
      for obj in Transferencias: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def Inserir():
    clientes = view.Cliente_Listar()
    cliente = st.selectbox("Selecione o cliente", clientes)
    contas = view.Conta_Listar()
    conta1 = st.selectbox("Selecione a conta para realizar a transferencia", contas)
    conta2 = st.selectbox("Selecione a conta para receber a transferencia", contas)
    Data_De_Transferencia = datetime.datetime.now()
    Saldo_Da_Transferencia = st.number_input("Informe o Saldo Da tranferencia")
    if st.button("Inserir"):
      try:
        view.Transferencia_Inserir(cliente.get_id(),conta1.get_id(),conta2.get_id(),Data_De_Transferencia, Saldo_Da_Transferencia)
        st.success("Transferencia inserida com sucesso")
        time.sleep(2)
        st.rerun()
      except Exception as erro:
        st.error(erro)
        st.error("Informações invalidas")
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
      contas = view.Conta_Listar()
      conta1_atual = view.Conta_Listar_Id((op.get_id_Conta1()))
      if conta1_atual is not None:
        conta1 = st.selectbox("Selecione o nova conta para transferencia", contas, contas.index(conta1_atual))
      else:
        conta1 = st.selectbox("Selecione o nova conta para transferencia", contas)
      conta2_atual = view.Conta_Listar_Id((op.get_id_Conta2()))
      if conta2_atual is not None:
        conta2 = st.selectbox("Selecione o nova conta para deposito", contas, contas.index(conta2_atual))
      else:
        conta2 = st.selectbox("Selecione o nova conta para deposito", contas)
      if st.button("Atualizar"):
        try:
          data = datetime.datetime.strptime(Data_De_Transferencia,"%d/%m/%Y %H:%M")
          view.Transferencia_Atualizar(op.get_id(), cliente.get_id(),conta1.get_id(),conta2.get_id(), data, Saldo_Da_Transferencia)
          st.success("Transferencia atualizada com sucesso")
          time.sleep(2)
          st.rerun()
        except Exception as erro:
          st.error(erro)
          st.error("Informações invalidas") 
  def Excluir():
    Transferencias = view.Transferencia_Listar()
    if len(Transferencias) == 0:
      st.write("Nenhuma Conta Cadastrada")
    else:
      op = st.selectbox("Exclusão de Transferencia", Transferencias)
      if st.button("Excluir"):
        view.Transferencia_Excluir(op.get_id())
        st.success("Transferencia excluida com sucesso")
        time.sleep(2)
        st.rerun()
