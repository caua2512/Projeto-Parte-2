import streamlit as st
from View import view
import pandas as pd

class ListarContasUI:
  def main():
    st.header("Controlar Bancos")
    ListarContasUI.Listar()
  def Listar():
    id_logado = st.session_state["cliente_id"]
    contas = view.listar_contas_do_cliente(id_logado)
    if len(contas) == 0:
      st.write("Nenhuma Conta cadastrada")
    else:
      dic = []
      for obj in contas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)



