import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

tabela = "CREATE TABLE IF NOT EXISTS usuarios (usuario_id text PRIMARY KEY,\
    nome text, idade int, cidade text)"

usuario = "INSERT INTO usuarios VALUES ('quinto', 'Jorge', '34', 'Bahia')"

cursor.execute(tabela)
cursor.execute(usuario)

conexao.commit()
conexao.close()
