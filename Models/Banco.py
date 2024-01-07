from Models.Modelo import Modelo
import json

class Banco:
    def __init__(self, id, nome, endereco, clientes = []):
        self.__id = id
        self.__nome = nome
        self.__endereco = endereco
        self.__clientes = clientes
        if nome == "": raise ValueError("Informações invalidas")
        if endereco == "": raise ValueError("Informações invalidas")

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_endereco(self): return self.__endereco
    def get_clientes(self): return self.__clientes

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): 
        if nome == "": raise ValueError("Informações invalidas")
        self.__nome = nome
    def set_endereco(self, endereco): 
        if endereco == "": raise ValueError("Informações invalidas")
        self.__endereco = endereco
    def set_clientes(self, clientes): self.__clientes = clientes

    def adiciona_cliente(self, cliente_id):
        self.__clientes.append(cliente_id)
    
    def remove_cliente(self, cliente_id):
        self.__clientes.remove(cliente_id)

    def __eq__(self, banco):
        return self.__id == banco.__id and self.__nome == banco.__nome and self.__endereco == banco.__endereco

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__endereco}"
    

class NBanco(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("bancos.json", mode="r") as arquivo:
                bancos_json = json.load(arquivo)
                for obj in bancos_json:
                    banco = Banco(obj["_Banco__id"], 
                                  obj["_Banco__nome"], 
                                  obj["_Banco__endereco"],
                                  obj["_Banco__clientes"])
                    cls.objetos.append(banco)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("bancos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

    
