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

vagas = 30
veiculos = []


def cadastrar():
    placa = input("Informe a placa do seu veículo: \n")
    if len(veiculos) == vagas:
            print(f"O estacionamento esta lotado, aguarde novas vagas!")
    elif placa not in veiculos:
        veiculos.append(placa)
        print(f"O veículo {placa} foi cadastrado com sucesso!")
    else:
        print(f"O veículo {placa} ja esta cadastrado no sistema")

while True:
    print("===== GERENCIAMENTO DE ESTACIONAMENTO =====")
    print("1 - Cadastrar Veículo ")
    print("2 - Registrar Saída ")
    print("3 - Listar Veículos")
    print("4 - Listar Vagas Disponíveis ")
    print("5 - Sair")
    print("="*44)
    opcao = int(input("Escolha uma opção \n"))

    if opcao == 5:
        break
    elif opcao == 1:
        cadastrar()
        continuar = input("Deseja voltar ao menu principal? [S/N]").lower()
        if continuar == "s":
            print(" ")
        else:
            # Aqui vai o valor ficticio na hora da saída
            break








print("\n" + "=" * 50)
print("       ESTACIONAMENTO ENCERRADO!")
print("       Obrigado por utilizar nosso sistema.")
print("=" * 50)