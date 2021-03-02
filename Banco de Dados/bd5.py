import sqlite3
import random
import time
import datetime
import os
os.remove("dse.db") if os.path.exists("dse.db") else None
import matplotlib as mat

#Criando uma conexão
conn = sqlite3.connect('dse.db')

#criando um cursor

c = conn.cursor()

#Função para criar uma tabela
def create_table():
    c.execute('CREATE TABELE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , date TEXT,'\
              'prod_name TEXT , valor REAL)')

#função para inserir uma linha
def data_insert():
    c.execute("INSERT INTO produtos VALUES('2018-05-02  12:34:45','Teclado', 130.00)")
    conn.commit()
    c.close()
    conn.close()

#usando varíaveis para inserir dados
def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = 'Monitor'
    new_valor = random.randrange(50,100)
    c.execute("INSERT INTO produtos (date , prod_name , valor) VALUES (?,?,?)",(new_date, new_prod_name,new_valor))
    conn.commit()

#leitura de dados
def leitura_todos_dados():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha)

#leitura de dados específicos
def leitura_registros():
    c.execute("SELECT * FROM PRODUTOS WERE valor > 60.0")
    for linha in c.fetchall():
        print(linha)

#leitura de colunas especificas
def leitura_colunas():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha[3])

#update
def atualiza_dados():
    c.execute("UPDATE produtos SET valor = 70.00  WHERE valor = 98.0")
    conn.commit()

#delete
def remove_dados():
    c.execute("DELETE FROM produtos WHERE valor  = 62.0")
    conn.commit()

atualiza_dados()
leitura_todos_dados()
remove_dados()
leitura_registros()
leitura_colunas()
c.close()
conn.close()

