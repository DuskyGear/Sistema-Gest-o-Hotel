from cliente import Cliente
from apartamento import Apartamento
from endereco import Endereco
from datetime import *

class Hotel():
    __valortotal=0.0
    def __init__(self):
        self.__Clientes = dict()
        self.__Apartamentos = dict()
        
    
    def getclientes(self):
        return self.__Clientes
    

    def setclientes(self,outrosclientes):
        self.__Clientes = outrosclientes


    def getapartamentos(self):
        return self.__Apartamentos
    

    def setapartamentos(self,outrosapartamentos):
        self.__Apartamentos = outrosapartamentos
  
#cadastro de clientes ultilizado o dicionario para armazenar as informaçoes,a chave do dicionario será a combinação das 3 primeiras letras do nome do cliente
#e toda extenção do cpf
    def cadastroCliente(self):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        rg = input("Digite seu rg: ")
        telefone = input("Digite o telefone: ")
        logra = input("Digite seu Logradouro: ")
        tipo = input("Endentificação de endereço RUA/AVENIDA/PRAÇA : ")
        numero = input("Digite o numero da casa: ")
        bairro = input("Digite o bairro: ")
        cep = input("Digite o CEP: ")
        cidade = input("Digite a cidade: ")
        uf = input("Digite o UF: ")

        newend = Endereco(logra,tipo,numero,bairro,cep,cidade,uf)
        newcliente = Cliente(nome,cpf,rg,newend,telefone)
        
        self.__Clientes.setdefault(newcliente.getCodC(),newcliente)

#O cadastro do apartamento foi ultilizado o dicionario para armazenar as informaçoes,a chave do dicionario é a numero do apartamento
    def cadastroApartamento(self):
        n = input("Digite O numero do quarto:")
        if n in self.__Apartamentos.keys():
            print("ESSE QUARTO JÁ EXISTE")
        else:
            dataE=""
            dataS=""
            tipo = input("Digite o tipo do apartamento: ")
            totaldesp =0.0
            codHosped =""
            telefone =""
            situacao ="L"
            nunreserva=""

            newApart = Apartamento(situacao,dataE,dataS,tipo,totaldesp,codHosped,telefone,nunreserva) 
            self.__Apartamentos.setdefault(n,newApart)

#O for percorrerá por todo o dicionario de apartamentos, exibindo todas as informaçoes.
    def statusOcupacao(self):
        for chave,apart in self.__Apartamentos.items():
            
            print(f"Apartamento: {chave}")
            print(f"Tipo de Apartamento: {apart.getTipo()}")
            print(f"Situação: {apart.getSituacao()}")
            print(f"Data de Entrada: {apart.getDataE()}")
            print(f"Data de Saida: {apart.getDataS()}")
            print(f"Telefone: {apart.getFone()}")
            print(f"Total de despesas: {apart.getTotalDesp()}")
            print(f"Codigo: {apart.getCodigoC()} ")
            print("="*30)
        input("PRESSIONE ENTER PARA CONTINUAR.....")
            
#O for percorrerá por todo o dicionario de apartamentos, exibindo somente os apartamentos com status "O"
    def listadeOcupacao(self):
        for key,ocupado in self.__Apartamentos.items():
            if ocupado.getSituacao()=="O":
            
                print(f"Apartamento: {key}")
                print(f"Situação: {ocupado.getSituacao()}")
                print(f"Data de entrada: {ocupado.getDataE()}")
                print(f"Data de Saida: {ocupado.getDataS()}")
                print(f"Tipo: {ocupado.getTipo()}")
                print(f"Total de despesas: {ocupado.getTotalDesp()}")
                print(f"Codigo do hospede: {ocupado.getCodigoC()}")
                print(f"Telefone: {ocupado.getFone()}")
                print(f"-"*30)
        input("PRESSIONE ENTER PARA CONTINUAR.....")

#Será feito testes em diversas ocasioes que poderia dar erro, checagem de disponibilidade de apartamento e checagem de cpf.
#Será mostardo ao cliente os apartamentos disponiveis e o tipo de acomodação
#será coletados dados de entrada e saida e serão setados todos dentro do apartamento escolhido
    def chekinNormal(self):

        valord= 0
        cpf = input("Digite o CPF  do Cliente: ")

        if len(self.__Apartamentos)==0:
            print("NÃO EXISTE APARTAMENTOS CADASTRADOS ")
        elif self.verificaApart()==0:
            print("NÃO TEMOS APARTAMENTOS DISPONIVEIS PARA ALOCAR")
        elif self.verificaCpf(cpf)==0:
            print(f"Cpf não consta no nosso banco de dados!")
            
        
        else:
            for keys,cli in self.__Clientes.items():
                if cpf == cli.getCpf():
                    print(f"="*30)
                    cli.exibirCliente()
                    print(f"="*30)
            codigo=input("Digite o codigo do cliente: ")        
            print("QUARTOS DISPONIVEIS:")
            for key,ocupado in self.__Apartamentos.items():
                if ocupado.getSituacao()=="L":
                            
                    print(f"Apartamento: {key}")
                    print(f"Situação: {ocupado.getSituacao()}")
                    print(f"Tipo: {ocupado.getTipo()}")
                    print(f"-"*30)
                            
            numero = input("Digite o numero do Quarto: ")
            print(f"="*30)
            print("DATA DE ENTRADA:")
            print(f"="*30)
            day = int (input('Dia: '))
            moth = int (input('Mes: '))
            year = int (input('Ano: '))
            dataE = (date(year,moth,day))
            status="O"
            print(f"="*30)
            print("DATA DE SAIDA:")
            print(f"="*30)
            day1 = int (input('Dia: '))
            moth1 = int (input('Mes: '))
            year1 = int (input('Ano: '))
            dataS = (date(year1,moth1,day1))
            quantidade_dias = abs((dataE - dataS).days)
                    
            for key,apart in self.__Apartamentos.items():
                if key==numero :
                    for chave,cliente in self.__Clientes.items():
                        if chave==codigo:
                            apart.setSituacao(status)
                            apart.setFone(cliente.getTelefone())
                            apart.setDataE(dataE)
                            apart.setDataS(dataS)
                            if apart.getTipo()=="S":
                                valord = 150.0
                            if apart.getTipo()=="D":
                                valord = 250.0
                            if apart.getTipo()=="T":
                                valord = 300.0
                            if apart.getTipo()=="C":
                                valord = 350.0
                            totalhospedagem=valord*quantidade_dias
                            apart.setAdicionarValor(totalhospedagem)
                            apart.setCodigoC(codigo)
                            self.logChekin(numero,codigo,dataE)
                    
#Será feito uma busca percorrendo o dicionario de apartamento e será adicionado o valor solicitado ao total de despesas do quarto(somado as eventuais despesas)
    def despesas(self):
        apartamento = input("Digite o apartamento: ")
        valor = float(input("Digite o valor a ser adicionado: "))
        for key,apart in self.__Apartamentos.items():
            if key==apartamento:
                apart.setAdicionarValor(valor)
                print("VALOR ADICIONADO COM SUCESSO!")

#Será checado se há apartamentos disponiveis,caso seja encontrado será coletado a data prevista e alguns dados serão alocados no apartamento(O status do apartamento será modificado para "R")
    def reserva(self):
        
        cpf = input("Digite o CPF:  ")

        if len(self.__Apartamentos)==0:
            print("NÃO EXISTE APARTAMENTOS CADASTRADOS")
        elif self.verificaApart()==0:
            print("NÃO TEMOS APARTAMENTOS DISPONIVEIS PARA ALOCAR")
        elif self.verificaCpf(cpf)==0:
            print(f"CPF não encontrado no nosso banco de dados!")
        else:
            for keys,cli in self.__Clientes.items():
                if cpf == cli.getCpf():
                    print(f"="*30)
                    cli.exibirCliente()
                    print(f"="*30)
            cadastro = input("Codigo do cadastro: ")
            print("Os apartamentos disponiveis são: ")
            for key,ocupado in self.__Apartamentos.items():
                if ocupado.getSituacao()=="L":
                            
                    print(f"Apartamento: {key}")
                    print(f"Situação: {ocupado.getSituacao()}")
                    print(f"Tipo: {ocupado.getTipo()}")
                    print(f"-"*30)
                            
                            
            numero = input("Digite o numero do Quarto: ")
            print(f"="*30)
            print("DATA PREVISTA DE ENTRADA:")
            print(f"="*30)
            day = int (input('Dia: '))
            moth = int (input('Mes: '))
            year = int (input('Ano: '))
            dataE = (date(year,moth,day))
            status="R"

            for key,apart in self.__Apartamentos.items():
                if key==numero :
                    for chave,cliente in self.__Clientes.items():
                        if chave==cadastro:
                            apart.setSituacao(status)
                            apart.setDataE(dataE)
                            apart.setCodigoC(cadastro)
                            apart.setFone(cliente.getTelefone())
                            break
                                       
        input("PRESSIONE ENTER PARA CONTINUAR......")

#Será feito testes em diversas ocasioes que poderia dar erro, checagem de disponibilidade de apartamento e checagem de cpf.
#Será alocado os dados igualmente ao chekin normal porem a busca será percorrida atras do codigo vinculado ao quarto e o status ser "R"
    def chekinReserva(self):
        status="O"
        cpf = input("Digite o Cpf: ")

        if self.verificaCpf(cpf)==0:
            print(f"CPF não encontrado no nosso banco de dados!")
        else:
            for keys,cli in self.__Clientes.items():
                if cpf == cli.getCpf():
                    print(f"="*30)
                    cli.exibirCliente()
                    print(f"="*30)
            
            valord=0
            codigo = input("Digite o codigo do Cliente: ")
            self.verificaReserva(codigo)
            apartamento=input("Informe o apartamento Reservado: ")
            for key,apart in self.__Apartamentos.items():
                if key==apartamento:
                    for keys,cliente in self.__Clientes.items():
                        if apart.getCodigoC()==codigo:
                            apart.setSituacao(status)
                            apart.setFone(cliente.getTelefone())
                            print(f"="*30)
                            print("DATA DE SAIDA:")
                            print(f"="*30)
                            day1 = int (input('Dia: '))
                            moth1 = int (input('Mes: '))
                            year1 = int (input('Ano: '))
                            dataS = (date(year1,moth1,day1))
                                    
                            if apart.getTipo()=="S":
                                valord = 150.0
                            if apart.getTipo()=="D":
                                valord = 250.0
                            if apart.getTipo()=="T":
                                valord = 300.0
                            if apart.getTipo()=="C":
                                        valord = 350.0

                            quantidade_dias = abs((apart.getDataE() - dataS).days)
                            dati=apart.getDataE()
                                    
                            totalhospedagem=valord*quantidade_dias
                            apart.setAdicionarValor(totalhospedagem)
                            apart.setDataS(dataS)
                            self.logChekin(apartamento,codigo,dati)
                            break
                                
        input("PRESSIONE ENTER PARA CONTINUAR......")

#Será checado a existencia do quarto informado,e printado todas as informaçoes e será informado o valor total a se pagar, além do valor total a pagar ser atribuido ao total arrecadado pelo resort
    def checkOut(self):
        situacao ="L"
        dataE=""
        dataS=""
        codigo=""
        telefone = ""
        totaldesp = 0.0
        nunap = input("Digite o numero do quarto: ")
        for key,apart in self.__Apartamentos.items():
            if key==nunap:
                print(f"Apartamento: {key}")
                print(f"Tipo de Apartamento: {apart.getTipo()}")
                print(f"Data de entrada: {apart.getDataE()}")
                print(f"Data de Saida: {apart.getDataS()}")
                print(f"Telefone: {apart.getFone()} ")
                print(f"Total a pagar: {apart.getTotalDesp()}")
                print(f"Codigo: {apart.getCodigoC()}")
                codigocli = apart.getCodigoC()
                datasaida = apart.getDataS()
                totaldespeca= apart.getTotalDesp()
                self.__valortotal = self.__valortotal + apart.getTotalDesp()
                self.logCheckout(nunap,codigocli,datasaida,totaldespeca)
                
                dc=input("Finalizar check out?")
                if dc=="Sim":
                    apart.setSituacao(situacao)
                    apart.setDataE(dataE)
                    apart.setDataS(dataS)
                    apart.setCodigoC(codigo)
                    apart.setFone(telefone)
                    apart.setTotalDesp(totaldesp)
        input("PRESSIONE ENTER PARA CONTINUAR......")

#Será percorrido e printado somente os apartamentos que se encontram ocupados durente a solicitação
    def relatorio1(self):

        for key,apt in self.__Apartamentos.items():
            if apt.getSituacao()=="O":
                print(f"Apartamento: {key}")
                print(f"Data de Checkin: {apt.getDataE()}")
                for keys,apto in self.__Clientes.items():
                    if keys==apt.getCodigoC():
                        print(f"Cliente: {apto.getNome()}")
                        print("-"*30)
        print("-"*30)
        input("PRESSIONE ENTER PARA CONTINUAR......")

#Será percorrido e printado somente os apartamentos que se encontram Reservados durente a solicitação
    def relatorio2(self):

        for key,apt in self.__Apartamentos.items():
            if apt.getSituacao()=="R":
                print(f"Apartamento: {key}")
                print(f"Data prevista para o Checkin: {apt.getDataE()}")
                for keys,apto in self.__Clientes.items():
                    if keys==apt.getCodigoC():
                        print(f"Cliente: {apto.getNome()}")
                        print("-"*30)
        print("-"*30)
        input("PRESSIONE ENTER PARA CONTINUAR......")

#Será percorrido e printado somente os apartamentos que se encontram Livres durente a solicitação
    def relatorio3(self):
        valordi=0
        for key,apt in self.__Apartamentos.items():
            if apt.getSituacao()=="L":
                print(f"Apartamento: {key}")
                print(f"Tipo: {apt.getTipo()}")
                if apt.getTipo()=="S":
                    valordi=150
                if apt.getTipo()=="D":
                    valordi=250
                if apt.getTipo()=="T":
                    valordi=300
                if apt.getTipo()=="C":
                    valordi=350
                print(f"Valor da diaria: {valordi}")
                print("-"*30)
        print("-"*30)
        input("PRESSIONE ENTER PARA CONTINUAR......")
    
#Será printado o total arrecadado pelo Resort
    def relatorio4(self):
        print(f"TOTAL ARRECADADO PELO HOTEL: {self.__valortotal}")
        input("PRESSIONE ENTER PARA CONTINUAR......")

#Pré molde de um log chekin, aonde será passado parametros e será registarado em um arquivo txt na pasta do arquivo
    def logChekin(self,numap,codigo,datae):
        arquivo = open("Log_chek_in.txt", "a")
        arquivo.write(f"APARTAMENTO: {numap},CODIGO DO CLIENTE: {codigo}, DATA DE ENTRADA: {datae}\n")
        arquivo.close()

#Pré molde de um log chek out, aonde será passado parametros e será registarado em um arquivo txt na pasta do arquivo
    def logCheckout(self,numap,codigo,datas,valor):
        arquivo = open("Log_chek_out.txt", "a")
        arquivo.write(f"APARTAMENTO: {numap},CODIGO DO CLIENTE: {codigo}, DATA DE Saida: {datas}, Valor da Hospedagem: {valor}\n")
        arquivo.close()

#Será percorrido todo o dicionario de Clientes e motras todos os clientes que já se encontram cadastrados.
    def relatorio5(self):

        for info in self.__Clientes.values():
            info.exibirCompleto()
            print("-"*30)
        input("PRESSIONE ENTER PARA CONTINUAR......")
        
#Metodo auxiliar para verificar a existencia do cpf
    def verificaCpf(self,cpf):
        cont=0
        for info in self.__Clientes.values():
            if info.getCpf()==cpf:
                cont+=1
        return cont
        
#Metodo auxiliar para verificar a existencia de Apartamentos Livres
    def verificaApart(self):

        cont=0
        for key,sit in self.__Apartamentos.items():
            if sit.getSituacao() =="L":
                cont+=1
        return cont
    
#Metodo auxiliar para verificar a existencia de Apartamento Reservado e printar qual apartamento foi reservado
    def verificaReserva(self,codigo):
        cont=0
        for key,info in self.__Apartamentos.items():
            if info.getCodigoC()==codigo:
                print(f"O apartamento {key} foi reservado pelo Cliente! ")
                cont+=1
        return cont

            