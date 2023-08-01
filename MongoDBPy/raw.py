from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/") #faz a conexao com o server do mongo
db_connection = client["meuBanco"]

# print("Conexao Base Dados: ", db_connection) #pode usar pra verificar se conseguiu conectar com o banco de dados ou não e se conectou com a base de dados certa

collection = db_connection.get_collection("minhaCollection")

#print("Conexao Colecao: ", collection) #pode usar pra verificar se conseguiu conectar com o banco de dados ou não e se conectou com a coleção certa

#BUSCA DE DADOS

search_filter = {"ola":"mundo"} #filtro de busca no json
# search_filter = {"ola":"diogo"} #filtro de busca no json
response = collection.find(search_filter)  #encontra os registros do json que possuem o filtro e retorna todas as informações do json que contém esse dicionário específico

for registro in response:
    print("Resgisto Encontrado", registro)

print("Resposta", response)


#INSERÇÃO DE DADOS

# collection.insert_one(
#     {
#         "Estou": "inserindo",
#         "Numeros": [123,456,789]
#     }
# )