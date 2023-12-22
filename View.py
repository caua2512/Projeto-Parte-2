from Models.Conta import Conta, NConta
from Models.Cliente import Cliente, NCliente
from Models.Banco import Banco, NBanco
import datetime

class view:
    def Banco_Listar():
        return NBanco.listar()
    def Banco_Listar_Id():
        return NBanco.get_banco(id)
    def Banco_Inserir(nome, endereço):
        return NBanco.inserir(0, nome, endereço)
    def Banco_Atualizar(id, nome, endereço):
        return NBanco.atualizar(id, nome, endereço)
    def Banco_Excluir(id):
        return NBanco.excluir(id," "," ")
    def Cliente_Listar():
        return NCliente.Listar()
    def Cliente_Listar_Id(id):
        return NCliente.Listar_id(id)
    def Cliente_Inserir( id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha):
        NCliente.inserir(Cliente(0,id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha))
    def Cliente_Atualizar(id, id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha):
        NCliente.Atualizar(Cliente(id, id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha))
    def Cliente_Excluir(id):
        NCliente.Excluir(Cliente(id, 0, " ", " ", " "," "," "," "))
    def Cliente_Admin():
        for cliente in view.Cliente_Listar():
            if cliente.get_Nome() == "admin": return
        view.Cliente_Inserir(0,"admin","data","Admin.Banco@gmail.com","000.000.000-00", "+00 (00) 00000-0000", "SenhaAdmin")   
    def Cliente_Login(email, senha):
        for cliente in view.Cliente_Listar():
            if cliente.get_Email() == email and cliente.get_Senha == senha:
                return cliente
        return None
    def Cliente_Editar_Perfil(id, id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha):
        NCliente.Atualizar(Cliente(id, id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha))
    def Conta_Listar():
        return NConta.Listar()
    def Conta_Listar_Id(id):
        return NConta.Listar_id(id)
    def Conta_Inserir( id_Cliente, Data_De_Abertura, Numero_Do_Banco, Saldo):
        NConta.inserir(Conta(0,id_Cliente, Data_De_Abertura, Numero_Do_Banco, Saldo))
    def Conta_Atualizar(id, id_Cliente, Data_De_Abertura, Numero_Do_Banco, Saldo):
        NConta.Atualizar(Conta(id, id_Cliente, Data_De_Abertura, Numero_Do_Banco, Saldo))
    def Conta_Excluir(id):
        NConta.Excluir(Conta(id, 0, " ", " ", " "))
    def listar_contas_do_cliente(clienteI):
        Contas_Do_Cliente = []
        for Conta in view.Conta_Listar():
            if Conta.get_id_Cliente() == clienteI:
                Contas_Do_Cliente.append(Conta)
        return Contas_Do_Cliente
    def depositar(Depositar):
        for conta in view.listar_contas_do_cliente():
            NConta.atualizar(Conta(conta.get_id(), conta.get_id_Cliente(), conta.get_Data_De_Abertura(), conta.Get_Numero_Do_Banco(), conta.get_saldo + Depositar))
    def sacar(Sacar):
        for conta in view.listar_contas_do_cliente():
            NConta.atualizar(Conta(conta.get_id(), conta.get_id_Cliente(), conta.get_Data_De_Abertura(), conta.Get_Numero_Do_Banco(), conta.get_saldo - Sacar))
    def transferir(id_conta1, id_conta2, Transferencia):
        conta1 =  view.Conta_Listar_Id(id_conta1)
        conta2 =  view.Conta_Listar_Id(id_conta2)
        view.Conta_Atualizar(id_conta1, conta1.get_id_Cliente(), conta1.get_Data_De_Abertura(), conta1.Get_Numero_Do_Banco(), conta1.get_saldo() - transferencia)
        view.Conta_Atualizar(id_conta2, conta2.get_id_Cliente(), conta2.get_Data_De_Abertura(), conta2.Get_Numero_Do_Banco(), conta2.get_saldo() + transferencia)
    def Listar_Minhas_Transferencias():
        Transferencias = []
        for transferencia in view.listar_contas_do_cliente():
            if transferencia.get_id_Cliente == view.transferir().get_id_Cliente:
                Transferencias.append(transferencia)
        return Transferencias




