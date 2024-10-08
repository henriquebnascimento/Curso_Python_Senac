contas = {}
def criar_conta():
    conta = int(input('Digite o número da conta: '))
    if conta in contas:
        print('Essa conta já exite')
    else:
        contas.append[conta]['saldo':0]
        
def ver_saldo():
    conta = int(input('Digite o número da conta: '))
    if conta in contas:
        print("O saldo atual na conta é {contas[conta]['saldo']}")
    

# def depositar

# def sacar

# def encerrar