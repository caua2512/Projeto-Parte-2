from Models.Modelo import Modelo
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
        if Nome == "": raise ValueError("Informações invalidas")
        if Data_De_Nascimento == "": raise ValueError("Informações invalidas")
        if Email == "": raise ValueError("Informações invalidas")
        if cpf == "": raise ValueError("Informações invalidas")
        if Fone == "": raise ValueError("Informações invalidas")
        if Senha == "": raise ValueError("Informações invalidas")

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
        if nome == "": raise ValueError("Informações invalidas")
    def get_Nome(self):
        return self.__Nome
    def set_Data_De_Nascimento(self, ddn):
        self.__Data_De_Nascimento = ddn
        if ddn == "": raise ValueError("Informações invalidas")
    def get_Data_De_Nascimento(self):
        return self.__Data_De_Nascimento
    def set_Email(self, email):
        self.__Email = email
        if email == "": raise ValueError("Informações invalidas")
    def get_Email(self):
        return self.__Email
    def set_CPF(self, cpf):
        self.__cpf = cpf
        if cpf == "": raise ValueError("Informações invalidas")
    def get_CPF(self):
        return self.__cpf
    def set_Fone(self, Fone):
        self.__Fone = Fone
        if Fone == "": raise ValueError("Informações invalidas")
    def get_Fone(self):
        return self.__Fone
    def set_Senha(self, senha):
        self.__Senha = senha
        if senha == "": raise ValueError("Informações invalidas")
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
    
class NCliente(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Clientes.json", mode="r") as arquivo:
                Clientes_json = json.load(arquivo)
                for obj in Clientes_json:
                    aux =  Cliente(obj["id"], obj["id_Banco"],obj["Nome"], datetime.datetime.strptime(obj["Data_De_Nascimento"], "%d/%m/%Y %H:%M"), obj["Email"], obj["CPF"], obj["Fone"], obj["Senha"])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Cliente.to_json)
