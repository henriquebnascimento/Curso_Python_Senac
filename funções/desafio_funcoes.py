# Criando um sistema que permita ao usuário realizar operações bancárias

# Banking system

def criar_conta():
    conta = input("Digite o número da conta: ")
    if conta in contas:
        print("Conta já existe!")
    else:
        contas[conta] = {"saldo": 0}
        print(f"Conta {conta} criada com sucesso.")

def verificar_saldo():
    conta = input("Digite o número da conta: ")
    if conta in contas:
        print(f"Saldo da conta {conta}: R$ {contas[conta]['saldo']:.2f}")
    else:
        print("Conta não encontrada!")

def depositar_dinheiro():
    conta = input("Digite o número da conta: ")
    if conta in contas:
        valor = float(input("Digite o valor a depositar: R$ "))
        contas[conta]['saldo'] += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Conta não encontrada!")

def sacar_dinheiro():
    conta = input("Digite o número da conta: ")
    if conta in contas:
        valor = float(input("Digite o valor a sacar: R$ "))
        if valor <= contas[conta]['saldo']:
            contas[conta]['saldo'] -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente!")
    else:
        print("Conta não encontrada!")

def menu():
    print("\n--- Sistema Bancário ---")
    print("1. Criar Conta")
    print("2. Verificar Saldo")
    print("3. Depositar Dinheiro")
    print("4. Sacar Dinheiro")
    print("5. Encerrar Atendimento")

# Programa principal
contas = {}

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        criar_conta()
    elif opcao == "2":
        verificar_saldo()
    elif opcao == "3":
        depositar_dinheiro()
    elif opcao == "4":
        sacar_dinheiro()
    elif opcao == "5":
        print("Encerrando atendimento. Obrigado!")
        break
    else:
        print("Opção inválida! Tente novamente.")

