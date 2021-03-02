import os
os.remove("dsb.db") if os.path.exists("dsb.db") else None

import sqlite3

#Criando uma conexão

conn = sqlite3.connect('dsb.db')

#Criando um cursor
c = conn.cursor()

#Função para criar uma tabela

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, ' \
              'prod_name TEXT, valor REAL)')


#função para inserir uma linha
def data_insert():
    c.execute("INSERT INTO produtos VALUES (10 , '2018-05-02 14:32:11' , 'Teclado ',90)")
    conn.commit()
    c.close()
    conn.close()

#criar tabela
create_table()

#inserir dados
data_insert()