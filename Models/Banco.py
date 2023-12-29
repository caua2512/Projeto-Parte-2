import json

class Banco:
    def __init__(self, id, nome, endereco, clientes = []):
        self.__id = id
        self.__nome = nome
        self.__endereco = endereco
        self.__clientes = clientes

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_endereco(self): return self.__endereco
    def get_clientes(self): return self.__clientes

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_endereco(self, endereco): self.__endereco = endereco
    def set_clientes(self, clientes): self.__clientes = clientes

    def adiciona_cliente(self, cliente_id):
        self.__clientes.append(cliente_id)
    
    def remove_cliente(self, cliente_id):
        self.__clientes.remove(cliente_id)

    def __eq__(self, banco):
        return self.__id == banco.__id and self.__nome == banco.__nome and self.__endereco == banco.__endereco

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__endereco}"
    

class NBanco:
    __bancos = []  

    @classmethod
    def abrir(cls):
        cls.__bancos = []
        try:
            with open("bancos.json", mode="r") as arquivo:
                bancos_json = json.load(arquivo)
                for obj in bancos_json:
                    banco = Banco(obj["_Banco__id"], 
                                  obj["_Banco__nome"], 
                                  obj["_Banco__endereco"],
                                  obj["_Banco__clientes"])
                    cls.__bancos.append(banco)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("bancos.json", mode="w") as arquivo:
            json.dump(cls.__bancos, arquivo, default=vars)

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0  
        for banco in cls.__bancos:
            if banco.get_id() > id: id = banco.get_id()
        obj.set_id(id + 1)
        cls.__bancos.append(obj)  
        cls.salvar()
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__bancos
    
    @classmethod
    def get_banco(cls, id):
        cls.abrir()
        for obj in cls.__bancos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        banco = cls.get_banco(obj.get_id())
        if banco is not None:
            banco.set_nome(obj.get_nome())
            banco.set_endereco(obj.get_endereco())
            banco.set_clientes(obj.get_clientes())
            cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        banco = cls.get_banco(obj.get_id())
        if banco is not None:
            cls.__bancos.remove(banco)
            cls.salvar()