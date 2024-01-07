import streamlit as st
import pandas as pd
from View import view
class ListarTransferenciasUI:
  def main():
    st.header("Listas Minhas Transferencias")
    ListarTransferenciasUI.Listar()
  def Listar():
    id_logado = st.session_state["cliente_id"]
    transferencias = view.Listar_Minhas_Transferencias(id_logado)
    if len(transferencias) == 0:
      st.write("Nenhuma Conta cadastrada")
    else:
      dic = []
      for obj in transferencias: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)
