def autualizarProdutos():
    # funcao para atualiar por um produto
    id_produto = int(input('Digite o ID do produto que deseja atualizar:"'))
    novo_produto = input('Digite o novo nome do produto: ')
    nova_quantidade = input('Digite a nova quantidade: ')
    novo_valorUnit = input('Digite o novo valor unitário: ')
    novo_valorTotal = novo_valorUnit * nova_quantidade
    
    conn = criar_conexao.connect()
    conn.execute("""
                 UPDADE cadastroProdutos
                 SET produto = ?, quantidade = ?, valorUnit = ?, valorTotal = ?
                 WHERE id = ?""",
                 (novo_produto, nova_quantidade, novo_valorUnit, novo_valorTotal, novo_valorTotal))
    print(f"produto com ID {id_produto}")