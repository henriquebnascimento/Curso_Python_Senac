import sqlite3
conn = sqlite3.connect('produtos.db')

conn.execute('CREATE TABLE cadastroProdutos(id_produto INTEGER PRIMARY KEY AUTOINCREMENT, produto text, quantidade text, valorUnit real, valorTotal real)')

conn.commit()
conn.close()