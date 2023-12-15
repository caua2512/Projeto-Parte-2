from Models.Conta import Conta, NConta
from Models.Cliente import Cliente, NCliente
import datetime

class view:
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








