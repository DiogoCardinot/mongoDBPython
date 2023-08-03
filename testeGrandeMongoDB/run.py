from pymongo import MongoClient
import random
import timeit

client = MongoClient("mongodb://localhost:27017/") #faz a conexao com o server do mongo
db_connection = client["grandao"]

collection = db_connection.get_collection("enorme")


collection.update_many({}, {"$set":{"idade": 29} }) #coloca a idade de 29 em todos os registros



# data = collection.find({})

# for element in data:
#     collection.update_one({"idade":29},{"$set":{"idade": random.randint(10,95)}}) #altera a idade de todo mundo que tinha a idade igual a 29


idades = []
#salva todos os registros e verifica os que quer depois
data = collection.find({})

tempo_inicial_all_elements = timeit.default_timer()
for element in data:
    if(element["idade"] == 29):
        idades.append(element['idade'])
tempo_final_all_elements = timeit.default_timer()
tempoCalculo_all_elements = tempo_final_all_elements - tempo_inicial_all_elements
print(len(idades))
print("Tempo sem filtro nenhum:", tempoCalculo_all_elements, "\n\n")


#já verifica os que quer e só salva depois
idades1=[]
data1 = collection.find({"idade":29})
tempo_inicial_elements = timeit.default_timer()
for element in data1:
    idades1.append(element['idade'])
tempo_final_elements = timeit.default_timer()
tempoCalculo_elements = tempo_final_elements - tempo_inicial_elements
print(len(idades1))
print("Tempo com filtro:", tempoCalculo_elements)