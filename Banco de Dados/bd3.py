import sqlite3
import random
import time
import datetime
import os
os.remove("dsc.db") if os.path.exists("dsc.db") else None

#Criando uma conexão
conn = sqlite3.connect('dsc.db')

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

#gerando valores e inserindo na tabela
for i in range(10):
    data_insert_var()
    time.sleep(1)

#encerando a conexão
c.close()
conn.close()