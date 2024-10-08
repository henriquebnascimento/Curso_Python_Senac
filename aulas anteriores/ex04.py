def obter_informacoes_pedido():
    pedido = {    
        'item': 'Notebook',
        'preco': 1200.00,
        'quantidade': 2
    }
    print(f'Obtendo informaçoes do produto.')
    return pedido
        
def calcular_preco_total(pedido):
    preco_total = pedido['preco'] * pedido['quantidade']
    print(f"Valor total calculado: R${preco_total}")
    return preco_total

def enviar_confirmacao(pedido, preco_total):
    print(f"Confirmação enviada para {pedido['quantidade']} {pedido['item']}(s).")
    print(f"Valor total à pagar: R${preco_total}")

def processar_pedido():
    pedido = obter_informacoes_pedido()
    preco_total = calcular_preco_total(pedido)
    enviar_confirmacao(pedido, preco_total)
    
processar_pedido()