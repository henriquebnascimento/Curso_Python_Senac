import sqlite3

conn = sqlite3.connect('produtos.db')

def listarProdutos():
    conn.execute('')