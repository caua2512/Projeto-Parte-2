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
import streamlit as st

class IndexUI:

  def menu_temporario():
    op = st.sidebar.selectbox("Menu", ["Login","Abrir Conta Sistema","Editar Perfil","Abrir Conta","Manter Banco", "manter Cliente","Manter Contas","Depositar","Sacar","Transferir","Listar Transferencias"])
    if op == "Manter Banco": ManterBancoUI.main()
    if op == "manter Cliente": ManterClienteUI.main()
    if op == "Manter Contas": ManterContaUI.main()
    if op == "Login": loginUI.main()
    if op == "Abrir Conta Sistema": AbrirContaSistemaUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()
    if op == "Abrir Conta": AbrirContaUI.main()
    if op == "Listar Contas": ListarContasUI.main()
    if op == "Depositar": DepositarUI.main()
    if op == "Sacar": SacarUI.main()
    if op == "Transferir": TransferirUI.main()
    if op == "Listar Transferencias": ListarTransferenciasUI.main()
  
  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["cliente_id"]
      del st.session_state["cliente_nome"]
      st.rerun()

  def sidebar():
    if "cliente_id" not in st.session_state:
      IndexUI.menu_temporario()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
      IndexUI.btn_logout()  

  def main():
    IndexUI.sidebar()

IndexUI.main()
