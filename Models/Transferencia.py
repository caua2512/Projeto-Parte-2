from Models.Modelo import Modelo
import datetime
import json

class Transferencia:
    def __init__(self, id ,id_cliente, id_Conta1, id_Conta2, Data_De_Transferencia ,Saldo_da_transferencia):
        self.__id = id
        self.__id_cliente = id_cliente
        self.__id_Conta1 = id_Conta1
        self.__id_Conta2 = id_Conta2
        self.__Data_De_Transferencia = Data_De_Transferencia
        self.__Saldo_da_transferencia = Saldo_da_transferencia
    
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    def set_id_Cliente(self, idC):
        self.__id_cliente = idC
    def get_id_Cliente(self):
        return self.__id_cliente
    def set_id_Conta1(self, idc1):
        self.__id_Conta1 = idc1
    def get_id_Conta1(self):
        return self.__id_Conta1
    def set_id_Conta2(self, idc2):
        self.__id_Conta2 = idc2
    def get_id_Conta2(self):
        return self.__id_Conta2
    def set_Data_De_Transferencia(self, ddt):
        self.__Data_De_Transferencia = ddt
    def get_Data_De_Transferencia(self):
        return self.__Data_De_Transferencia
    def set_Saldo_da_transferencia(self, saldoT):
        self.__Saldo_da_transferencia = saldoT
    def get_Saldo_da_transferencia(self):
        return self.__Saldo_da_transferencia
    
    def __eq__(self, x):
        if self.__id == x.__id and self.__Data_De_Transferencia == x.__Data_De_Transferencia and self.__id_cliente == x.__id_cliente and self.__id_Conta1 == x.__id_Conta1 and self.__id_Conta2 == x.__id_Conta2 and self.__Saldo_da_transferencia == x.__Saldo_da_transferencia:
            return True
        return False 
    def __str__(self):
        return f"{self.__id} - {self.id_cliente} - {self.__id_Conta1} - {self.__id_Conta2} - {self.__Data_De_Transferencia.strftime('%d/%m/%Y %H:%M')} - {self.__Saldo_da_transferencia}"
    def to_json(self):
        return {
            "id": self.__id,
            "id_Cliente": self.__id_cliente,
            "id_Conta1": self.__id_Conta1,
            "id_Conta2": self.__id_Conta2,
            "Data_De_Transferencia": self.__Data_De_Transferencia.strftime('%d/%m/%Y %H:%M'),
            "Saldo_Da_Transferencia": self.__Saldo_da_transferencia
        }
    
class NTransferencia(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Transferencias.json", mode="r") as arquivo:
                Transferencias_json = json.load(arquivo)
                for obj in Transferencias_json:
                    aux =  Transferencia(obj["id"], datetime.datetime.strptime(obj["Data_De_Transferencia"], "%d/%m/%Y %H:%M"), obj["id_Cliente"], obj["id_Conta1"], obj["id_Conta2"], obj["Saldo_Da_Transferencia"])
                    cls.objetos.append(aux)
        except FileNotFoundError:
            pass
    
    @classmethod
    def salvar(cls):
        with open("Transferencias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)
