"""
14. Sistema de estacionamento 
Enunciado: Crie um programa para controlar a entrada e a saída de veículos em um estacionamento com número limitado de vagas. Para simplificar, registre a placa e o horário ou número sequencial de entrada.
 O programa deverá:  
 Definir a capacidade máxima do estacionamento. (FEITO)
 Registrar a entrada de um veículo, armazenando sua placa.  (FEITO)
 Impedir entrada quando todas as vagas estiverem ocupadas. (FEITO)
 Registrar a saída de um veículo pela placa. (FEITO)
 Impedir a saída de uma placa que não esteja estacionada. (FEITO)
 Exibir os veículos presentes e a quantidade de vagas livres. 
 Separar as operações em funções. 
 Desafio extra (opcional): Calcular um valor fictício de estacionamento conforme a quantidade de horas informada na saída. 
"""

vagas = 30
veiculos = ["Livre"] * vagas
tarifa = 5.00
def cadastrar():
    while True:
        placa = input("Informe a placa do seu veículo: \n")
        if placa == "":
            continuar = input("A placa informada é vazia, deseja digitar novamente? [S/N]").lower()
            if continuar == 's':
                 print()
            else:
                 break
        elif len(veiculos) - veiculos.count("Livre") == vagas: # A quantidade de veiculos estacionados é igual a capacidade maxima? se sim ele lota
                continuar = input(f"O estacionamento esta lotado, aguarde novas vagas, deseja continuar? [S/N]").lower()
                if continuar == 's':
                    print()
                else:
                    break        
        elif placa in veiculos:
            continuar = input(f"O veículo {placa} ja esta cadastrado no sistema, deseja continuar? [S/N]").lower()
            if continuar == 's':
                 print()
            else:
                 break
        elif "Livre" in veiculos:
            vaga = veiculos.index("Livre") + 1
            veiculos[veiculos.index("Livre")] = placa
            print(f"O veículo {placa} foi cadastrado com sucesso na vaga {vaga}!")
            break
        

def saida():
    # Aqui vai o valor ficticio na hora da saída
    while True:
        placasaida = input("Informe a placa do seu veículo para retirada \n")
        if placasaida in veiculos:
                vaga = veiculos.index(placasaida) + 1
                try:
                    horastarifa = int(input("Informe quantas horas seu veículo ficou estacionado \n"))
                    if horastarifa <= 0:
                        print("Valor invalido, por favor, informe um valor válido!")
                    else:
                        print(f"Foi cobrado uma tarifa de {tarifa*horastarifa} pelo uso do estacionamento")
                        veiculos[veiculos.index(placasaida)] = "Livre"
                        print(f"O veículo estacionado na vaga {vaga} que possui a placa: {placasaida} foi retirado do sistema!")  
                        break 
                except ValueError:
                            continuar = input("O valor digitado é invalido, deseja inserir novamente? [S/N]").lower()
                            if continuar == 's':
                                print()
                            else:
                                break       
        else:
            continuar = input(f"A placa {placasaida} não esta cadastrada no sistema, deseja informar novamente? [S/N]").lower()
            if continuar == 's':
                print()
            else:
                break


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
            break
    elif opcao == 2:
         saida()
         continuar = input("Deseja voltar ao menu principal? [S/N]").lower()
         if continuar == "s":
            print(" ")
         else:
            break







print("\n" + "=" * 50)
print("       ESTACIONAMENTO ENCERRADO!")
print("       Obrigado por utilizar nosso sistema.")
print("=" * 50)