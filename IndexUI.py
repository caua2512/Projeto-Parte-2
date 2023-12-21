from Templates.ManterBancoUI import ManterBancoUI
from Templates.ManterClienteUI import ManterClienteUI
from Templates.ManterContaUI import ManterContaUI
from Templates.LoginUI import loginUI
from Templates.AbrirContaSistemaUI import AbrirContaSistemaUI
from Templates.EditarPerfilUI import EditarPerfilUI
from Templates.AbrirContaBancoUI import AbrirContaUI
from Templates.Listar_Minhas_ContasUI import ListarContasUI
from Templates.SacarUI import SacarUI
from Templates.DepositarUI import DepositarUI
from Templates.TransferirUI import TransferirUI
from Templates.Listar_Transferencias_RecentesUI import ListarTransferenciasUI
from View import view
import streamlit as st

class IndexUI:
  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta Sistema"])
    if op == "Login": loginUI.main()
    if op == "Abrir Conta Sistema": AbrirContaSistemaUI.main()
  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Banco", "manter Cliente","Manter Contas","Editar Perfil"])
    if op == "Manter Banco": ManterBancoUI.main()
    if op == "manter Cliente": ManterClienteUI.main()
    if op == "Manter Contas": ManterContaUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()
  def menu_temporario():
    op = st.sidebar.selectbox("Menu", ["Editar Perfil","Abrir Conta","Depositar","Sacar","Transferir","Listar Transferencias"])
    if op == "Abrir Conta": AbrirContaUI.main()
    if op == "Listar Contas": ListarContasUI.main()
    if op == "Depositar": DepositarUI.main()
    if op == "Sacar": SacarUI.main()
    if op == "Transferir": TransferirUI.main()
    if op == "Listar Transferencias": ListarTransferenciasUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()

  
  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["cliente_id"]
      del st.session_state["cliente_nome"]
      st.rerun()

  def sidebar():
    if "cliente_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
      if st.session_state["cliente_nome"] == "admin": IndexUI.menu_admin()
      else: IndexUI.menu_cliente()
      IndexUI.btn_logout()  

  def main():
    view.cliente_admin()
    IndexUI.sidebar()

IndexUI.main()
