import streamlit as st
import pandas as pd
from View import view
import datetime
import time
class ManterClienteUI:
  def main():
    st.header("Controlar Cliente")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterClienteUI.Listar()
    with tab2: ManterClienteUI.Inserir()
    with tab3: ManterClienteUI.Atualizar()
    with tab4: ManterClienteUI.Excluir()    

  def Listar():
    clientes = view.Cliente_Listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      dic = []
      for obj in clientes: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)
  def Inserir():
    nome = st.text_input("Informe o nome")
    bancos = view.Banco_Listar()
    banco = st.selectbox("selecione Banco", bancos)
    Data_de_nascimento = st.text_input("Informe a data de nascimento em formato dd/mm/YYYY")
    email = st.text_input("Informe o e-mail")
    cpf = st.text_input("infrome o cpf")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      data = datetime.datetime.strptime(Data_de_nascimento, "%d/%m/%Y %H:%M")
      view.Cliente_Inserir(banco.get_id(), nome, data, email, cpf,fone, senha)
      st.success("Cliente inserido com sucesso")
      time.sleep(2)
      st.rerun()
  def Atualizar():
    clientes = view.Cliente_Listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("seleciona cliente para atualizar", clientes)
      bancos = view.Banco_Listar()
      banco_atual = view.Banco_Listar_Id(op.get_id_Banco())
      if banco_atual is not None:
        banco = st.selectbox("Selecione o Banco", bancos, bancos.index(banco_atual))
      else:
        banco = st.selectbox("Selecione o Banco", bancos)
      nome = st.text_input("Informe o nome", op.get_Nome())
      Data_de_nascimento = st.text_input("Informe a data de nascimento em formato dd/mm/YYYY", op.get_Data_De_Nascimento().strftime("%d/%m/%Y %H:%M"))
      email = st.text_input("Informe o e-mail", op.get_Email())
      cpf = st.text_input("infrome o cpf", op.get_CPF())
      fone = st.text_input("Informe o fone", op.get_Fone())
      senha = st.text_input("Informe a senha", op.get_Senha())
      if st.button("Atualizar"):
        try:
          data = datetime.datetime.strptime(Data_de_nascimento, '%d/%m/%Y %H:%M')
          view.Cliente_Atualizar(op.get_id(),banco.get_id(), nome, data, email, cpf, fone, senha)
          st.success("Cliente atualizado com sucesso")
          time.sleep(2)
          st.rerun()
        except:
          st.error("Informações invalidas")
  def Excluir():
    clientes = view.Cliente_Listar()
    if len(clientes) == 0:
      st.write("Nenhum cliente excluido")
    else:
      op = st.selectbox("seleciona cliente para excluir", clientes)
      if st.button("Excluir"):
        view.Cliente_Excluir(op.get_id())
        st.success("Cliente excluido com sucesso")
        time.sleep(2)
        st.rerun()
