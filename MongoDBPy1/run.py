from models.connection_options.connection import DBConnectionHandler
from models.repository.minhaCollection_repository import MinhaCollectionRepositoty

dbHandle = DBConnectionHandler()


# conn1 = dbHandle.get_db_connection() #verifica a conexao antes de conectar 

dbHandle.conect_to_db() #funcao para conectar ao banco de dados
db_connection = dbHandle.get_db_connection() #verifica a conexao apos ter conectado, retorna algo


collection = db_connection.get_collection("minhaCollection")

minha_collection_repository = MinhaCollectionRepositoty(db_connection)


filter = {"listaDesejos.modelo":"Dunk Low", "listaDesejos.precoDesejado":{"$lte":410} } #filtro and, tem q satisfazer os dois ao mesmo tempo
#filtro or no minhaCollection_repository (lte é menor ou igual)

# filter = {"quantidade": {"$lte":500}}
# returnOptions = {"_id":0, "user":1, "listaDesejos.categoria":1, "listaDesejos.modelo":1, "listaDesejos.precoDesejado":1} #retorna apenas os usuários, o id e a categoria

returnOptions = {"_id":0, "user":1} #retorna apenas os usuários, o id e a categoria


#CASO DO TCC
responseContacts = minha_collection_repository.select_contact(filter,returnOptions)
# print("Contatos\n", responseContacts)

#BUSCA
responseSelectMany = minha_collection_repository.select_many(filter, returnOptions)
responseSelectOne = minha_collection_repository.select_one(filter, returnOptions)
# minha_collection_repository.select_if_property_exists() #verifica se existe registro de acordo com aluma propriedade
# minha_collection_repository.select_manyOrdered()

# minha_collection_repository.select_or_filter() #teste do filtro or
# print(responseSelectMany, "\n")
# print(responseSelectOne, "\n")


#EDIÇÃO
nome = "Diogo"
filtro = {"name": "Diogo"}
propriedade = {"Profissao": "Dev", "idade":22} #caso não exista o campo ele cria e insere
# minha_collection_repository.edit_many_registries(filtro, propriedade)

#INCREMENTO
# minha_collection_repository.edit_many_increment(4) #aumenta o valor
# minha_collection_repository.edit_many_increment(-2) #diminui o valor


#DELETE
minha_collection_repository.delete_registry()




# print("conexao", conn1)
# print('conn', conn2)
# print("Colecao", collection)

# collection.insert_one(
#     {
#         "user": "552230664496",
#         "listaDesejos":[
#             {
#                 "categoria": "Roupa",
#                 "marca": "Adidas",
#                 "itemDesejado": "Camiseta",
#                 "modelo": "Real Madrid",
#                 "precoDesejado": 120
#             },
#             {
#                 "categoria": "Roupa",
#                 "marca": "Nike",
#                 "itemDesejado": "Tênis",
#                 "modelo": "Dunk Low",
#                 "precoDesejado": 550
#             }
#         ]
#     }
# )


#BUSCA
# search_filter = {"user": "5522992770045"} #filtro de busca no json
# # search_filter = {"ola":"mundo"} #filtro de busca no json
# response = collection.find(search_filter)  #encontra os registros do json que possuem o filtro e retorna todas as informações do json que contém esse dicionário específico

# for registro in response:
#     print("Resgisto Encontrado", registro)

# print("Resposta", response)


# order = {
#     "name": "Diogo",
#     "endereco": "Rua procurando",
#     "pedidos": {
#         "pizza":"1",
#         "refrigerante":"2",
#         "batata":"1"
#     }
# }

# registro = {
#         "user": "552278910",
#         "listaDesejos":[
#             {
#                 "categoria": "Eletronicos",
#                 "marca": "MSI",
#                 "itemDesejado": "Placa de Vídeo",
#                 "modelo": "4070 Gaming X TRIO",
#                 "precoDesejado": 3500
#             },
#             {
#                 "categoria": "Roupas",
#                 "marca": "Nike",
#                 "itemDesejado": "Tênis",
#                 "modelo": "Dunk Low",
#                 "precoDesejado": 575
#             }
#         ]
# }

# minha_collection_repository.insert_document(registro) #inserir um documento apenas no bd

# list_of_documents = [
#     {"nissan": "skyline"},
#     {"lamborghini":"revuelto"},
#     {"ford": "mustang"},
#     {"toyota":"supra"}
# ]
# minha_collection_repository.insert_list_of_documents(list_of_documents) #insere vários documentos, mas cada um com um registro diferente no bd