from models.connectionsBD.connection import DBConnectionHandler

from datetime import datetime

dbHandle = DBConnectionHandler()

dbHandle.conect_to_db()
dbConnection = dbHandle.get_db_connection()

collection = dbConnection.get_collection("ListaDesejos")

produto = "Dunk Low Pink"
preco = 310

contacts = []

# data = collection.find({"modelo":'Dunk Low', "precoDesejado":{"$lte":550}})



#verifica se existe algum na lista de desejos com interesse no item que chegou e no preço
data = collection.find({}) #pega todos os registros do banco de dados
for element in data: #pra cada registro
    if (element["modelo"] in produto and  preco <= element["precoDesejado"] and int(element["user"]) not in contacts):
        contacts.append(int(element['user']))


#se existir, verifica se essa mensagem já chegou em determinado intervalo de tempo
if len(contacts) >=1: #envia pra base de dados o histórico de produtos que bateram no preço desejado
    collectionHistorico = dbConnection.get_collection("Historico")
    data1 = collectionHistorico.count_documents({"product": produto, "price": preco})
    dataCompare = collectionHistorico.find({"product": produto, "price": preco})

    # for element in dataCompare:
    #     print(element['date'])
    #     print(element['hour'])


    if data1 == 0: #verifica se já existe algum documento 
        dataCompleta = datetime.now()  #dia e hora
        DataHorario = str(dataCompleta).split() #separa os dois

        today = DataHorario[0] #dia de hoje

        horaAtual = DataHorario[1]

        collectionHistorico.insert_one({
                "product": produto,
                "price": preco,
                "date":today,
                "hour": horaAtual
        })
    else:
        contacts = []
        print(contacts)
        print("Já Tem")
    
    print("Contatos:", contacts)



#SEPARA A HORA E DATA ATUAL
data_e_hora_atuais = datetime.now()

DataHoraAtual = str(data_e_hora_atuais).split()
DataAtual  = DataHoraAtual [0].split("-")
DayAtual  = str(DataAtual [2])
MonthAtual  = str(DataAtual [1])
YearAtual  = str(DataAtual [0])

HoraCompletaAtual  = DataHoraAtual [1].split(":")
HourAtual  = str(HoraCompletaAtual [0])
MinutesAtual  = str(HoraCompletaAtual [1])
SecondsExtensiveAtual  = str(HoraCompletaAtual [2])
SecondsSplitAtual  = SecondsExtensiveAtual .split(".")
SecondsAtual  = SecondsSplitAtual [0]

now = datetime(int(YearAtual ), int(MonthAtual ), int(DayAtual ), int(HourAtual), int(MinutesAtual ), int(SecondsAtual )) #yr, mo, day, hr, min, sec

#SEPARA DATA E HORA QUE VEM DO BD

collectionHistorico = dbConnection.get_collection("Historico")


dataCompare = collectionHistorico.find({"product": produto, "price": preco}).sort([("_id", -1)]).limit(1) #ordeno o retorno de forma que o primeiro id seja o mais recente

for element in dataCompare:
    print(element['_id'])
    DataBD  = str(element['date']).split("-")

    DayBD  = str(DataBD[2])
    MonthBD  = str(DataBD[1])
    YearBD  = str(DataBD[0])
    # print(DayBD, '/', MonthBD, '/', YearBD)

    HoraCompletaBD = str(element['hour']).split(":")
    
    HourBD  = str(HoraCompletaBD[0])
    MinutesBD  = str(HoraCompletaBD[1])
    SecondsExtensiveBD  = str(HoraCompletaBD[2])
    SecondsSplitBD  = SecondsExtensiveBD .split(".")
    SecondsBD  = SecondsSplitBD[0]

    


bd = datetime(int(YearBD), int(MonthBD), int(DayBD), int(HourBD), int(MinutesBD), int(SecondsBD))

minutesDiference = ((now-bd).total_seconds())/60
print ("Diferenca de Minutos", minutesDiference)

