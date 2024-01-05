from Models.Modelo import Modelo
import datetime
import json

class Conta:
    def __init__(self, id , id_Cliente , Data_De_Abertura , Numero_Do_Banco , Saldo ):
        self.__id = id
        self.__id_Cliente = id_Cliente
        self.__Data_De_Abertura = Data_De_Abertura
        self.__Numero_Do_Banco = Numero_Do_Banco
        self.__Saldo = Saldo
    
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    def set_id_Cliente(self, idc):
        self.__id_Cliente = idc
    def get_id_Cliente(self):
        return self.__id_Cliente
    def set_Data_De_Abertura(self, dda):
        self.__Data_De_Abertura = dda
    def get_Data_De_Abertura(self):
        return self.__Data_De_Abertura
    def set_Numero_Do_Banco(self, ndb):
        self.__Numero_Do_Banco = ndb
    def get_Numero_Do_Banco(self):
        return self.__Numero_Do_Banco
    def set_Saldo(self, saldo):
        self.__Saldo = saldo
    def get_saldo(self):
        return self.__Saldo
    
    def __eq__(self, x):
        if self.__id == x.__id and self.__Data_De_Abertura == x.__Data_De_Abertura and self.__id_Cliente == x.__id_Cliente and self.__Numero_Do_Banco == x.__Numero_Do_Banco and self.__Saldo == x.__Saldo:
            return True
        return False 
    def __str__(self):
        return f"{self.__id} - {self.__id_Cliente} - {self.__Data_De_Abertura.strftime('%d/%m/%Y %H:%M')} - {self.__Numero_Do_Banco} - {self.__Saldo}"
    def to_json(self):
        return {
            "id": self.__id,
            "id_Cliente": self.__id_Cliente,
            "Data_De_Abertura": self.__Data_De_Abertura.strftime('%d/%m/%Y %H:%M'),
            "Numero_Do_banco": self.__Numero_Do_Banco,
            "Saldo": self.__Saldo
        }
    
class NConta(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Contas.json", mode="r") as arquivo:
                Contas_json = json.load(arquivo)
                for obj in Contas_json:
                    aux =  Conta(obj["id"], obj["id_Cliente"], datetime.datetime.strptime(obj["Data_De_Abertura"], "%d/%m/%Y %H:%M"), obj["Numero_Do_banco"], obj["Saldo"])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass
    
    @classmethod
    def salvar(cls):
        with open("Contas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Conta.to_json)
