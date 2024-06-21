from apartamento import Apartamento
from endereco import Endereco 
class Cliente():
    def __init__(self,nome,cpf,rg,endereco,telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__endereco = endereco
        self.__telefone = telefone
        self.__codC = self.__geraCod(nome,cpf)

    def getNome(self):
        return self.__nome
    

    def setNome(self,outronome):
        self.__nome = outronome
    

    def getCpf(self):
        return self.__cpf
    

    def setCpf(self,outrocpf):
        self.__cpf = outrocpf


    def getRg(self):
        return self.__rg
    

    def setRg(self,outrorg):
        self.__rg = outrorg


    def getEndereco(self):
        return self.__endereco
    

    def setEndereco(self,outroendereco):
        self.__endereco = outroendereco


    def getCodC(self):
        return self.__codC
    

    def getTelefone(self):
        return self.__telefone
    

    def setTelefone(self,outrotelefone):
        self.__telefone = outrotelefone
    

    def setCodC(self,outrocodC):
        self.__codC = outrocodC


    def __geraCod(self,nome,cpf):
        self.__codC = nome[0:3].lower()+str(cpf)
        return self.__codC


    def exibirCliente(self):
        print(f"Nome: {self.__nome}")
        print(f"Codigo do cliente: {self.__codC}")
    

    def exibirCompleto(self):
        print(f"Nome: {self.__nome} ")
        print(f"Codigo: {self.__codC} ")
        print(f"RG: {self.__rg} ")
        print(f"CPF: {self.__cpf}")
        print(f"Telefone: {self.__telefone} ")
        print(f"Logra: {self.__endereco.getLogra()} ")
        print(f"Tipo de endereço: {self.__endereco.getTipoE()}")
        print(f"Numero da casa: {self.__endereco.getNumero()} ")
        print(f"Cidade: {self.__endereco.getCidade()} ")
        print(f"UF: {self.__endereco.getUf()} ")
        print(f"CEP: {self.__endereco.getCep()} ")
        print(f"Bairro: {self.__endereco.getBairro()} ")
    
    