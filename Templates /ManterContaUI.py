import streamlit as st
class ManterContaUI:
  def main():
    st.header("Controlar Bancos")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterContaUI.Listar()
    with tab2: ManterContaUI.Inserir()
    with tab3: ManterContaUI.Atualizar()
    with tab4: ManterContaUI.Excluir()    

  def Listar():
    pass
  def Inserir():
    DataDeAbertura = st.date_input("Informe o nome")
    Saldo = st.number_input("Informe o Saldo atual")
    if st.button("Inserir"):
      pass
  def Atualizar():
    DataDeAbertura = st.date_input("Informe o nome")
    Saldo = st.number_input("Informe o Saldo atual")
    if st.button("Atualizar"):
      pass
  def Excluir():
    pass
