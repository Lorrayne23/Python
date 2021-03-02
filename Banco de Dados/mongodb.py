
# Importamos o MongoClient para conectar nossa aplicação ao MongoDB
from pymongo import MongoClient
# Estabelecemos a conexão ao Banco de Dados
conn = MongoClient('localhost', 27017)



# Uma única instância do MongoDB pode suportar diversos bancos de dados
#Vamos criar o banco de dados cadastrodb

db = conn.cadastrodb

# Uma coleção é um grupo de documentos armazenados no MongoDB
# (relativamente parecido com o conceito de tabelas em bancos relacionais)
collection = db.cadastrodb

# Uma nota importante sobre coleções (e banco de dados ) em MongoDB é que eles são
# criados posteriormente - nenhum dos comandos acima executou efetivamente
# qualquer operação no servidor MongoDB . Coleções e banco de dados são criados quando o primeiro documento é inserido

import datetime

# Dados no MongoDB são representados(e armazenados) usando documentos JSON (javaScript Object Notation).Com o PyMongo usamos dicionários para representar documentos

post1 = { "codigo " : "ID-9987725",
          "prod_name" : "Geladeira",
          "marcas": ["brastemp","consul1","eletroluz"],
           "data_cadastro": datetime.datetime.utcnow()}
collection = db.posts
post_id = collection.insert_one(post1)
post_id.inserted_id

#Quando um documento é inserido uma chave especial, "_id", é adicionada
# automaticamente se o documento ainda não contém uma chave "_id".



post2 = { "codigo " : "ID-2209876",
          "prod_name" : "Televisor",
          "marcas": ["samsung","panasonic","lg"],
           "data_cadastro": datetime.datetime.utcnow()}

collection = db.posts

post_id = collection.insert_one(post2).inserted_id

collection.find_one({"prod_name" : "Televisor"})

# A função find() retorna um cursor e podemos então navegar pelos dados
for post in collection.find():
    print(post)

#Verificando o nome do banco de dados
print(db.name)

#verificar collections disponíveis
print(db.collection_name())








