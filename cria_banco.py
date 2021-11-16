import sqlite3

connecttion = sqlite3.connect('banco.db')
cursor = connecttion.cursor() #cursor serve para selecionar as coisas no bd

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
     nome text, estrelas real, diaria real, cidade text)"

cursor.execute(cria_tabela)

connecttion.commit()
connecttion.close()