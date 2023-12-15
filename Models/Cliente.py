import datetime
import json

class Cliente:
    def __init__(self, id , id_Banco , Nome , Data_De_Nascimento , Email, cpf , Fone, Senha):
        self.__id = id
        self.__id_Banco = id_Banco
        self.__Nome = Nome
        self.__Data_De_Nascimento = Data_De_Nascimento
        self.__Email = Email
        self.__cpf = cpf
        self.__Fone = Fone
        self.__Senha = Senha



    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    def set_id_Banco(self, idb):
        self.__id_Banco = idb
    def get_id_Banco(self):
        return self.__id_Banco
    def set_Nome(self, nome):
        self.__Nome = nome
    def get_Nome(self):
        return self.__Nome
    def set_Data_De_Nascimento(self, ddn):
        self.__Data_De_Nascimento = ddn
    def get_Data_De_Nascimento(self):
        return self.__Data_De_Nascimento
    def set_Email(self, email):
        self.__Email = email
    def Get_Email(self):
        return self.__Email
    def set_CPF(self, cpf):
        self.__cpf = cpf
    def get_CPF(self):
        return self.__cpf
    def set_Fone(self, Fone):
        self.__Fone = Fone
    def Get_Fone(self):
        return self.__Fone
    def set_Senha(self, senha):
        self.__Senha = senha
    def get_Senha(self):
        return self.__Senha
    
    def __eq__(self, x):
        if self.__id == x.__id and self.__id_Banco == x.__id_Banco and self.__Nome == x.__Nome and self.__Data_De_Nascimento == x.__Data_De_Nascimento and self.__Email == x.__Email and self.__cpf == x.__cpf and self.__Fone == x.__Fone and self.__Senha == x.__Senha:
            return True
        return False 
    def __str__(self):
        return f"{self.__id} - {self.__id_Banco} - {self.__Nome} - {self.__Data_De_Nascimento.strftime('%d/%m/%Y %H:%M')} - {self.__Email} - {self.__cpf} - {self.__Fone} - {self.__Senha}"
    def to_json(self):
        return {
            "id": self.__id,
            "id_Banco": self.__id_Banco,
            "Nome": self.__Nome,
            "Data_De_Nascimento": self.__Data_De_Nascimento.strftime('%d/%m/%Y %H:%M'),
            "Email": self.__Email,
            "CPF": self.__cpf,
            "Fone": self.__Fone,
            "Senha": self.__Senha
        }
    
class NCliente:
    __Clientes = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__Clientes:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__Clientes.append(obj)
        cls.salvar()
    
    @classmethod
    def Listar(cls):
        cls.abrir()
        return cls.__Clientes
    
    @classmethod
    def Listar_id(cls, obj):
        cls.abrir()
        for obj in cls.__Clientes:
            if obj.get_id() == id: return obj
        return None
    
    @classmethod
    def Atualizar(cls, obj):
        cls.abrir()
        aux = cls.Listar_id(obj.get_id())
        if aux is not None:
            aux.set_id_Banco(obj.get_id_Banco())
            aux.set_Nome(obj.Get_Nome())
            aux.set_Data_De_Nascimento(obj.get_Data_De_Nascimento())
            aux.set_Email(obj.get_Email())
            aux.set_CPF(obj.Get_CPF())
            aux.set_Fone(obj.get_Fone())
            aux.set_Senha(obj.get_Senha())
            cls.salvar()

    @classmethod
    def Excluir(cls, obj):
        cls.abrir()
        aux = cls.Listar_id(obj.get_id())
        if aux is not None:
            cls.__Clientes.remove(obj)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__Clientes = []
        try:
            with open("Clientes.json", mode="r") as arquivo:
                Clientes_json = json.load(arquivo)
                for obj in Clientes_json:
                    aux =  Cliente(obj["id"], obj["id_Banco"], datetime.datetime.strptime(obj["Data_De_Nascimento"], "%d/%m/%Y %H:%M"), obj["Email"], obj["CPF"], obj["Fone"], obj["Senha"])
                    cls.__Clientes.append(aux)
        except FileNotFoundError:
            pass
    
    @classmethod
    def salvar(cls):
        with open("Clientes.json", mode="w") as arquivo:
            json.dump(cls.__Clientes, arquivo, default=Cliente.to_json)
