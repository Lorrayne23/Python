#remove o arquivo com o banco de dados SQLite ( caso exista )
import os
os.remove("escola.db") if os.path.exists("escola.db") else None

#importando o módulo de acesso ao SQLite
import sqlite3

#cria uma conexão com o banco de dados
#se o banco de dados não existir , ele é criado neste momento
con = sqlite3.connect('escola.db')

type(con)

#criando um cursor
#Um cursor permite percorrer todos os registros em um conjunto de dados
cur = con.cursor()
type(cur)

#cria instrução sql

sql_create = 'create table cursos '\
    '(id integer primary key, '\
    'titulo varchar(100),'\
    'categoria varchar(140))'
#executando a instrução sql no cursor
cur.execute(sql_create)

#criando outra sentença SQL para inserir registro

sql_insert = ' insert into cursos values (?,?,?)'

#Dados

recset = [(1000, 'Ciência de Dados ', 'Data Science '),
          (1001,'Big Data Fundamentos', 'Big Data'),
          (1002,'Python Fundamentos','Análise de Dados')]

#inserindo registros

for rec in recset:
    cur.execute(sql_insert, rec)

#grava a transação
con.commit()

#criando outra sentença SQL para selecionar registros
sql_select = 'select * from cursos'

#seleciona todos os os registros e recupera os registros
cur.execute(sql_select)
dados = cur.fetchall()

#Mostra
for linha in dados:
    print('Curso Id : %d , Título : %s , Categoria : %s \n' % linha)


recset = [(1003,'Gestão de Dados com MongoDB','Big Data'),
          (1004,'R Fundamentos','Análise de Dados')]

#inserindo os registros
for rec in recset:
    cur.execute(sql_insert,rec)

#gravando transação
con.commit()

#seleciona todos os registros
cur.execute('select * from cursos')

#recupera os resultados
recset = cur.fetchall()

#mostra
for rec in recset:
    print('Curso Id : %d , Título : %s , Categoria : %s \n' % rec)

con.close









