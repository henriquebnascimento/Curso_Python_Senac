import sqlite3
conn = sqlite3.connect('produtos.db')  # Estabelecendo a conexão com o banco

def cadastro_prod():
    produto = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade: '))
    valorUnit = float(input('Digite o valor unit: '))
    valorTotal = valorUnit * quantidade                    

            
    conn.execute("INSERT INTO cadastroProdutos (produto, quantidade, valorUnit, valorTotal) VALUES (?, ?, ?, ?)", 
                                    (produto, quantidade, valorUnit, valorTotal))            
    conn.commit()
    print("Produto cadastrado com sucesso!")
    while True:
        escolha = int(input('O que deseja fazer?\n1. Cadastrar novo produto. \n2. Sair do programa. \nOpção escolhida: '))
        if escolha == 1:
            cadastro_prod()
            conn.close()  
        else:
            print('Saindo do programa...')
        break
   
cadastro_prod()
