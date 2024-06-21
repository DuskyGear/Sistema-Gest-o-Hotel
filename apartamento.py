class Apartamento():
    
    def __init__(self,situacao,dataE,dataS,tipo,totaldesp,codigoC,fone,qtdaparts):
        self.__situacao = situacao
        self.__dataE = dataE
        self.__dataS = dataS
        self.__tipo = tipo
        self.__totaldesp = totaldesp
        self.__codigoC = codigoC
        self.__fone = fone
        self.__qtdaparts = qtdaparts

    def getSituacao(self):
        return self.__situacao
    
    
    def setSituacao(self,outrasituacao):
        self.__situacao = outrasituacao


    def getDataE(self):
        return self.__dataE
    
    
    def setDataE(self,outradataE):
        self.__dataE = outradataE


    def getDataS(self):
        return self.__dataS
    
    
    def setDataS(self,outradataS):
        self.__dataS = outradataS


    def getTipo(self):
        return self.__tipo
    
    
    def setTipo(self,outrotipo):
        self.__tipo = outrotipo


    def getTotalDesp(self):
        return self.__totaldesp
    
    
    def setTotalDesp(self,outrototaldesp):
        self.__totaldesp = outrototaldesp


    def getCodigoC(self):
        return self.__codigoC
    
    
    def setCodigoC(self,outrocodigoC):
        self.__codigoC = outrocodigoC


    def getFone(self):
        return self.__fone
    
    
    def setFone(self,outrofone):
        self.__fone = outrofone

    
    def getNunreserv(self):
        return self.__qtdaparts
    
    
    def setNunreserv(self,qtdapart):
        self.__qtdaparts = qtdapart
        
#Será ultilizado como auxiliar na adicação de valores consumidos no resort
    def setAdicionarValor(self,valor):
        self.__totaldesp = self.__totaldesp + valor

    
        

    