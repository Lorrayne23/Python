import sqlite3
import random
import time
import datetime
import os

os.remove("dsd.db") if os.path.exists("dsd.db") else None
#Criando uma conexão
conn = sqlite3.connect('dsd.db')

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

leitura_todos_dados()
leitura_registros()
leitura_colunas()
c.close()
conn.close()
