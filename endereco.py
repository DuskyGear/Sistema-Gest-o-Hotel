class Endereco():
    def __init__(self,logra,tipo,numero,bairro,cep,cidade,uf):
        self.__logra =logra
        self.__numero = numero
        self.__bairro = bairro
        self.__cep = cep
        self.__cidade = cidade
        self.__uf = uf
        self.__tipo = tipo

    def getLogra(self):
        return self.__logra
    

    def setLogra(self,outrologra):
        self.__logra = outrologra


    def getTipoE(self):
        return self.__tipo
    
    
    def setTipoE(self,outroTipoE):
        self.__tipo = outroTipoE


    def getNumero(self):
        return self.__numero
    

    def setNumero(self,outronumero):
        self.__numero = outronumero


    def getBairro(self):
        return self.__bairro
    

    def setBairro(self,outrobairro):
        self.__bairro = outrobairro


    def getCep(self):
        return self.__cep
    

    def setCep(self,outrocep):
        self.__cep = outrocep


    def getCidade(self):
        return self.__cidade
    

    def setCidade(self,outracidade):
        self.__cidade = outracidade


    def getUf(self):
        return self.__uf
    
    
    def setUf(self,outrouf):
        self.__uf = outrouf
    
    