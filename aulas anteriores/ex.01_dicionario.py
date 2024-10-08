parcial = 0

def obter_detalhes_pedido():
# Simula a obtenção de detalhes de um pedido.
    lista_pedidos = []
    subtotal = 0
    while True:  
        item = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))
        quantidade = int(input('Digite a quantidade: '))
        subtotal += preco * quantidade
        
        pedido = {
            'item': item,
            'preco': preco,
            'quantidade': quantidade
        }
        lista_pedidos.append(pedido)
        print(f'Seu pedido foi adicionado com sucesso!')
        print(f'Parcial: R$ {subtotal:.2f}')
    
        while True:
            print('Deseja adicionar outro pedido? [s/n]\n********************************')
            escolha = str(input()).lower()
            if escolha == 's':                
                break
            elif escolha == 'n': 
                return lista_pedidos
            else:
                print('Opção inválida! Digite [s] para adicionar novo pedido ou [n] para exibir a lista de produtos.')
            

def calcular_preco_total(lista_pedidos):
    # Calcula o preço total do pedido.
        preco_total = sum(pedido['preco'] * pedido['quantidade'] for pedido in lista_pedidos)
        return preco_total
    
def enviar_confirmacao(lista_pedidos,preco_total):
    # Simula o envio de uma confirmação de pedido.
    for pedido in lista_pedidos:
        print(f"Confirmação enviada para {pedido['quantidade']} {pedido['item']}(s).")
    print(f'Valor total a ser pago: R${preco_total:.2f}')
    
def processar_pedido():
    # Chama as funções auxiliares para processar o pedido.
    
    lista_pedidos = obter_detalhes_pedido()
    preco_total = calcular_preco_total(lista_pedidos)
    enviar_confirmacao(lista_pedidos, preco_total)
    
    # Chamando a função principal
processar_pedido()