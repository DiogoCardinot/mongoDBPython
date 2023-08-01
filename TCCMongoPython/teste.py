from models.connectionsBD.connection import DBConnectionHandler

dbHandle = DBConnectionHandler()

dbHandle.conect_to_db()
dbConnection = dbHandle.get_db_connection()

collection = dbConnection.get_collection("ListaDesejos")

produto = "Dunk Low PRM 'Oxford Pink'"
preco = 450

contacts = []

data = collection.find({}) #pega todos os registros do banco de dados
for element in data: #pra cada registro
    if (element['modelo'] in produto and preco <= element['precoDesejado'] and int(element['user']) not in contacts):
        contacts.append(int(element['user']))

print(contacts)

# collection.insert_many([
   
#     {
#         "user": "5522992770524", 
#         "categoria": "Roupa",
#         "marca": "Nike",
#         "itemDesejado": "Tênis",
#         "modelo": "Dunk Low",
#         "precoDesejado": 550
#     },
#      {
#         "user": "5522992772947", 
#         "categoria": "Roupa",
#         "marca": "Nike",
#         "itemDesejado": "Tênis",
#         "modelo": "Dunk Low",
#         "precoDesejado": 449
#     },
#      {
#         "user": "5588", 
#         "categoria": "Roupa",
#         "marca": "Nike",
#         "itemDesejado": "Tênis",
#         "modelo": "Dunk Low",
#         "precoDesejado": 449
#     }

# ]
# )