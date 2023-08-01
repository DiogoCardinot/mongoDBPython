from pymongo import MongoClient
from .mongoDB_configs import mongo_db_infos

class DBConnectionHandler:
    def __init__(self) -> None:
        if mongo_db_infos["USERNAME"] == "" and mongo_db_infos["PASSWORD"] == "": #vertifica se a config do bd possui usuario e senha
            #faz o link para um bd sem login e senha
            self.__connection_string = "mongodb://{}:{}/".format(
                mongo_db_infos["HOST"],
                mongo_db_infos["PORT"]
            )
            
        else:
             #faz o link para um bd com login e senha
            self.__connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
                mongo_db_infos["USERNAME"],
                mongo_db_infos["PASSWORD"],
                mongo_db_infos["HOST"],
                mongo_db_infos["PORT"]
            )
        self.__database_name = mongo_db_infos["DB_NAME"] #pega o nome do banco de dados que quer usar, vindo do mongodb_configs
        self.__client = None #faz o client ser vazio, para atualiza-lo posteriormente
        self.__db_connection = None  #faz a conexão ser vazia, para atualiza-la posteriormente
        # print(self.__connection_string)
    
    def conect_to_db(self):
        self.__client = MongoClient(self.__connection_string) #atualiza o client com o link de conexao
        self.__db_connection = self.__client[self.__database_name] #atualiza qual banco de dados vai utilizar da conexao
    
    def get_db_connection(self):
        return self.__db_connection
    
    def get_db_client(self):
        return self.__client

        
