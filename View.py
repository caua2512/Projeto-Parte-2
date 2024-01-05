from Models.Conta import Conta, NConta
from Models.Cliente import Cliente, NCliente
from Models.Banco import Banco, NBanco
from Models.Transferencia import Transferencia, NTransferencia
import datetime

class view:
    def Banco_Listar():
        return NBanco.listar()
    def Banco_Listar_Id(id):
        return NBanco.listar_id(id)
    def Banco_Inserir(nome, endereço):
        return NBanco.inserir(Banco(0, nome, endereço))
    def Banco_Atualizar(id, nome, endereço):
        return NBanco.atualizar(Banco(id, nome, endereço))
    def Banco_Excluir(id):
        return NBanco.excluir(Banco(id," "," "))
    def Cliente_Listar():
        return NCliente.listar()
    def Cliente_Listar_Id(id):
        return NCliente.listar_id(id)
    def Cliente_Inserir( id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha):
        NCliente.inserir(Cliente(0,id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha))
    def Cliente_Atualizar(id, id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha):
        NCliente.atualizar(Cliente(id, id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha))
    def Cliente_Excluir(id):
        cliente = Cliente(id, 0, " ", " ", " "," "," "," ")
        NCliente.excluir(cliente)
    def Cliente_Admin():
        for cliente in view.Cliente_Listar():
            if cliente.get_Nome() == "admin": return
        view.Cliente_Inserir(0,"admin",datetime.datetime.strptime("25/12/2006 12:30", "%d/%m/%Y %H:%M"),"admin","admin", "admin", "admin")   
    def Cliente_Login(email, senha):
        for cliente in view.Cliente_Listar():
            if cliente.get_Email() == email and cliente.get_Senha() == senha:
                return cliente
        return None
    def Cliente_Editar_Perfil(id, id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha):
        NCliente.atualizar(Cliente(id, id_Banco, Nome, Data_De_Nascimento, Email, cpf, Fone, Senha))
    def Conta_Listar():
        return NConta.listar()
    def Conta_Listar_Id(id):
        return NConta.listar_id(id)
    def Conta_Inserir( id_Cliente, Data_De_Abertura, Numero_Do_Banco, Saldo):
        NConta.inserir(Conta(0,id_Cliente, Data_De_Abertura, Numero_Do_Banco, Saldo))
    def Conta_Atualizar(id, id_Cliente, Data_De_Abertura, Numero_Do_Banco, Saldo):
        NConta.atualizar(Conta(id, id_Cliente, Data_De_Abertura, Numero_Do_Banco, Saldo))
    def Conta_Excluir(id):
        NConta.excluir(Conta(id, 0, " ", " ", " "))
    def listar_contas_do_cliente(id_clienteLogado):
        Contas_Do_Cliente = []
        for Conta in view.Conta_Listar():
            if Conta.get_id_Cliente() == id_clienteLogado:
                Contas_Do_Cliente.append(Conta)
        return Contas_Do_Cliente
    def depositar(id, Depositar):
        for conta in view.Conta_Listar():
            NConta.atualizar(Conta(conta.get_id(), conta.get_id_Cliente(), conta.get_Data_De_Abertura(), conta.get_Numero_Do_Banco(), conta.get_saldo() + Depositar))
    def sacar(id,Sacar):
        for conta in view.Conta_Listar():
            NConta.atualizar(Conta(conta.get_id(), conta.get_id_Cliente(), conta.get_Data_De_Abertura(), conta.get_Numero_Do_Banco(), conta.get_saldo() - Sacar))
    def Transferencia_Listar():
        return NTransferencia.listar()
    def Transferencia_Listar_Id(id):
        return NTransferencia.get_Transferencia(id)
    def Transferencia_Inserir(id_Cliente,id_Conta1, id_Conta2, Data_De_Transferencia, Saldo_Da_Transferencia):
        return NTransferencia.inserir(Transferencia(0,id_Cliente,id_Conta1, id_Conta2, Data_De_Transferencia, Saldo_Da_Transferencia))
    def Transferencia_Atualizar(id,id_Cliente,id_Conta1, id_Conta2, Data_De_Transferencia, Saldo_Da_Transferencia):
        return NTransferencia.atualizar(Transferencia(id,id_Cliente, id_Conta1, id_Conta2, Data_De_Transferencia, Saldo_Da_Transferencia))
    def Transferencia_Excluir(id):
        return NTransferencia.excluir(Transferencia(id,0,0,0," "," "))            
    def transferir(id_conta1, id_conta2, Transferencia):
        conta1 =  view.Conta_Listar_Id(id_conta1)
        conta2 =  view.Conta_Listar_Id(id_conta2)
        view.Transferencia_Inserir(conta1.get_id_Cliente(),conta1.get_id(), conta2.get_id(), datetime.datetime.now(), Transferencia)
        view.Transferencia_Inserir(conta2.get_id_Cliente(),conta1.get_id(), conta2.get_id(), datetime.datetime.now(), Transferencia)
        view.Conta_Atualizar(conta1.get_id(), conta1.get_id_Cliente(), conta1.get_Data_De_Abertura(), conta1.get_Numero_Do_Banco(), conta1.get_saldo() - Transferencia)
        view.Conta_Atualizar(conta2.get_id(), conta2.get_id_Cliente(), conta2.get_Data_De_Abertura(), conta2.get_Numero_Do_Banco(), conta2.get_saldo() + Transferencia)
    def Listar_Minhas_Transferencias(id_ClienteLogado):
        Transferencias_do_cliente = []
        for Transferencia in view.Transferencia_Listar():
            if Transferencia.get_id_Cliente() == id_ClienteLogado:
                Transferencias_do_cliente.append(Transferencia)
        return Transferencias_do_cliente         


                
