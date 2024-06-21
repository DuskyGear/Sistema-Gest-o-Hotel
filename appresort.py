from hotel import Hotel
from time import sleep

hotel = Hotel()
opc=""

def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

#Menu principal
def menu_p():
    
    cabeçalho("HOTEL PORTO CABRALIA")
    print('''
            MENU PRINCIPAL

            [1] - Cadastro
            [2] - Status de ocupação
            [3] - Lista de ocupação
            [4] - Chek In /Reserva apartamento
            [5] - Lançamento despesas extras
            [6] - Chek Out
            [7] - Relatórios
            [0] - Sair
        ''') 
    

##menu de cadastro
def menu_c():
   print('''
            MENU DE CADASTRO

            [1] - Cadastrar Clientes
            [2] - Cadastrar Apartamento
            [3] - Voltar para o Menu Principal
            [0] - Sair
            
        ''') 
   

##menu de checkin
def menu_check():
    print('''
            MENU DE CHECKIN
            
            [1] - Realizar CheckIn
            [2] - Realizar Reserva
            [3] - Realizar Checkin por reserva
            [4] - Voltar para o Menu Principal
            [0] - Sair
            
        ''')


##menu de relatorios
def menu_r():
    print('''
            MENU DE RELATÓRIOS
            
            [1] - Apartamentos Ocupados
            [2] - Apartamentos Reservados
            [3] - Apartamentos Livres
            [4] - Total Arrecadado pelo Resort
            [5] - Lista de Clientes
            [6] - Voltar para o Menu Principal
            [0] - Sair
        ''')


#Programa princial, responsavel por gerir as situaçoes do menu
while opc != '0':
    
    menu_p()
    opc = input ('Digite a opção desejada: ')
    
    match(opc):
        case '1':

            menu_c()
            opc = input ('Digite a opção desejada: ')
            
            
            if opc == '1':
                cabeçalho('Cadastro de Clientes')
                hotel.cadastroCliente()
                cabeçalho('Cadastro Finalizado')
                sleep(2)

            elif opc == '2':
                cabeçalho('Cadastro de Apartamentos')
                hotel.cadastroApartamento()
                cabeçalho('Cadastro Finalizado')
                sleep(2)
                


    
        case '2':
            cabeçalho('STATUS DE OCUPAÇÃO')
            hotel.statusOcupacao()
            sleep(2)
        
        case '3':
            cabeçalho('LISTA DE OCUPAÇÃO')
            hotel.listadeOcupacao()
            sleep(2)
        
        case '4':
            menu_check()
            opc = input ('Digite a opção desejada: ')
            
            if opc == "1":
                cabeçalho("CHECKIN NORMAL")
                hotel.chekinNormal()
                sleep(1)
            elif opc == "3":
                cabeçalho("CHEKIN RESERVA")
                hotel.chekinReserva()
                sleep(1)
            elif opc == '2':
                cabeçalho("RESERVA")
                hotel.reserva()
                cabeçalho("RESERVA FINALIZADA")
                sleep(1)
                

        case '5':
            cabeçalho("ADICIONAR DESPESAS")
            hotel.despesas()
            cabeçalho("ADICIONADO COM SUCESSO")
            sleep(1)
        
        case '6':
            cabeçalho("CHECK OUT")
            hotel.checkOut()
            sleep(1)
        
        case '7':
            menu_r()
            cabeçalho('RELATORIOS DE OCUPAÇÃO')
            opc = input ('Digite a opção desejada: ')
            if opc=='1':
                cabeçalho("Relatorio de Apartamentos Ocupados")
                hotel.relatorio1()
            elif opc=='2':
                cabeçalho("Relatorio de Apartamentos Reservados")
                hotel.relatorio2()
            elif opc=='3':
                cabeçalho("Relatorio de Apartamentos Livres")
                hotel.relatorio3()
            elif opc=='4':
                cabeçalho("Relatorio de total arrecadado pelo Resort")
                hotel.relatorio4()
            elif opc=="5":
                cabeçalho("Relatorio de Clientes")
                hotel.relatorio5()

            
        
        case '0':
            cabeçalho('FINALIZANDO O PROGRAMA..')
            sleep(2)        
        case other:
            cabeçalho('ERRO')
            cabeçalho('Opção invalida. Digite uma opção correta.')
            input('Pressione ENTER para continuar...')