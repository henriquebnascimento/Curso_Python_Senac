# Criando um programa que realize as seguintes operações bancárias.
# Criar conta - ok
# Verificar saldo - ok
# Depositar dinheiro - ok
# Sacar dinheiro - ok
# Encerrar o atendimento
def criar_conta():
    conta = input('Digite sua conta: ')
    if conta in contas:
        print('Essa conta já existe!')
    else:
        contas[conta] = {'saldo': 0}
    print(f"Conta {conta} criada com sucesso")
    
def verificar_saldo():
    conta = input('Digite o número de sua conta: ')
    if conta in contas:
        print(f"O Saldo atual da conta {conta} é de: R$ {contas[conta]['saldo']:.2f}.")
    else:
        print('Conta não encontrada!')  
        
def depositar_dinheiro():
    conta = input('Digite o número de sua conta:') 
    if conta in contas:
        valor = float(input("Informe o valor a depositar: R$ "))
        contas[conta]['saldo'] += valor
        print(f"O Depósito no valor de {valor:.2f} foi adicionado com sucesso!")
    else:
        print('Conta não encotrada!')
        
def sacar_dinheiro():
    conta = input('Digite o número de sua conta:')
    if conta in contas:
        valor = float(input('Qual o valor que deseja sacar? R$ '))
        if valor <= contas[conta]['saldo']:
            contas[conta]['saldo'] -= valor        
            print(f"O valor de {valor:.2f} foi sacado com sucesso!")
        else:
            print('Saldo insuficiente!')
    else:
        print('Conta não encontrada!')
        
        
def menu():
    print('\n--- Sistema Bancário ---')
    print('1. Criar uma Conta')
    print('2. Verificar Saldo')
    print('3. Depositar Dinheiro')
    print('4. Sacar Dinheiro')
    print('5. Encerrar Atendimento')
        
       

while True:
    menu ()
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Opção inválida. Texto não permitido.')   
    else:       
        
        if opcao == 1:
            criar_conta()
        elif opcao == 2:
            verificar_saldo()
        elif opcao == 3:
            depositar_dinheiro()
        elif opcao == 4:
            sacar_dinheiro()
        elif opcao == 5:
            print('Atendimento Finalizado. Obrigado!')
            break
        else:
            print('Número inválido. Digite novamente.')
    
# Função principal
contas = {}        