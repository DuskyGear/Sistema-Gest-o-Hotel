# Sistema-Gest-o-Hotel
Projeto desenvolvido no meu primeiro contato com Programação Orientada a Objeto em Python

#Sistema de Gestão de Hotel
Este projeto é um sistema de gestão de hotel que permite o cadastro de clientes, gerenciamento de apartamentos, check-in, check-out e a geração de relatórios diversos sobre o status de ocupação do hotel. A seguir, será detalhado o funcionamento de cada parte do sistema e como utilizá-lo.


Exemplo de Uso
Aqui está um exemplo básico de como utilizar o sistema de gestão de hotel:
from hotel import Hotel

# Criação do objeto Hotel
meu_hotel = Hotel()

# Cadastro de um cliente
meu_hotel.cadastroCliente()

# Cadastro de um apartamento
meu_hotel.cadastroApartamento()

# Realizar o check-in de um cliente
meu_hotel.chekinNormal()

# Adicionar despesas a um apartamento
meu_hotel.despesas()

# Realizar uma reserva
meu_hotel.reserva()

# Realizar o check-in de uma reserva
meu_hotel.chekinReserva()

# Realizar o check-out de um cliente
meu_hotel.checkOut()

# Gerar relatórios
meu_hotel.relatorio1()  # Apartamentos ocupados
meu_hotel.relatorio2()  # Apartamentos reservados
meu_hotel.relatorio3()  # Apartamentos livres
meu_hotel.relatorio4()  # Total arrecadado
meu_hotel.relatorio5()  # Clientes cadastrados
