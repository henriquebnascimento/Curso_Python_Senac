# try:
#     arquivo = open('função/Tratamento de Exeções/dados.txt','r')
#     conteudo = arquivo.read()
#     print(conteudo)
# except FileNotFoundError:
#     print('Arquivo não encontado.')
# finally:
#     print("Operação finalizada.")
    
    
# try:
#     arquivo = open('aulas anteriores/dados1.txt','r')
#     conteudo = arquivo.read()
#     print(conteudo)
# except FileNotFoundError:
#     print('Arquivo não encontado.')
# finally:
#     print("Operação finalizada.")


# try:
#     num = int(input('Digite um número: '))
#     resultado = 100 / num
# except ValueError:
#     print('Erro: Você deve digitar um número inteiro.')
    
# except (ValueError, TypeError): # psso tratar cada erro individualmente ou acrescentar todos e padronizar a mesma mensagem.
#     print('Erro. Divisão por zero não é permitida')    
# else:
#     print(f"O resultado é {resultado}")
    
# finally:
#     print('Obrigdo por usar o programa.')

# USANDO O RAISE
# def verifica_idade(idade):
#     if idade < 18:
#         print('Idade deve ser maior ou igual a 18.')
#     else:
#         print('Idade permitida')

# try:
#     verifica_idade(17)
# except ValueError as msg:
#     print(msg)
            
# def mostrar_texto(nome):
#     print(f'Olá {nome}')


# def outra_funcao(nome):
#     mostrar_texto(nome)
# outra_funcao("Henrique")

# COMO CRIAR UMA EXCEÇÃO PERSONALIZADA
 #Crie uma classe que herda de Exception ou de uma de suas subclasses
 
 # Exemple:
# class saldoInsuficienteError(Exception):
#      """Exceção levantada quando o saldo é insuficiente para realizar a operação."""
# pass

# def sacar(valor, saldo):
#     if valor > saldo:
#         raise saldoInsuficienteError('Saldo insuficiente para sacar o valor solicitado.')
#     saldo -= saldo
#     return saldo
# try:
#     saldo_atual = sacar(1500,1000)
# except saldoInsuficienteError as e:
#     print(e)
    
    
class saldoInsuficiente(Exception):
    pass

def sacar(valor, saldo):
    if valor > saldo:
        print('O Saldo em conta é insuficiente para realizar a operação.')
    else:
        saldo -= valor
        print(f"O valor de {valor:.2f} foi sacado com sucesso. Seu saldo em conta é de: R$ {saldo:.2f}")
try:
    saldo_em_conta = sacar(100, 130)
except saldoInsuficiente as msg:
    print(msg)