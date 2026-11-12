"""
14. Sistema de estacionamento 
Enunciado: Crie um programa para controlar a entrada e a saída de veículos em um estacionamento com número limitado de vagas. Para simplificar, registre a placa e o horário ou número sequencial de entrada.
 O programa deverá:  
 Definir a capacidade máxima do estacionamento. 
 Registrar a entrada de um veículo, armazenando sua placa. 
 Impedir entrada quando todas as vagas estiverem ocupadas. 
 Registrar a saída de um veículo pela placa. 
 Impedir a saída de uma placa que não esteja estacionada. 
 Exibir os veículos presentes e a quantidade de vagas livres. 
 Separar as operações em funções. 
 Desafio extra (opcional): Calcular um valor fictício de estacionamento conforme a quantidade de horas informada na saída. 
"""

capmax = 50
veiculos = []


while True:
    print("===== GERENCIAMENTO DE ESTACIONAMENTO =====")
    print("1 - Cadastrar Veículo ")
    print("2 - Registrar Saída ")
    print("3 - Listar Veículos")
    print("4 - Listar Placas Disponíveis ")
    print("5 - Sair")