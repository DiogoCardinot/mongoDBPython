from typing import Dict, List

class MinhaCollectionRepositoty:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "minhaCollection"
        self.__db_connection = db_connection
    #inserindo um unico documento
    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
    
    #inserindo uma lista de documentos
    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents
    #selecionando vários registros do banco de dados de acordo com o filtro e com as opçoes de retorno
    def select_many(self, filter, returnOptions) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filter, returnOptions)

        response = []
        for element in data:
            response.append(element["user"])
        return response
    #selecionando o primeiro registro do banco de dados de acordo com o filtro e com as opçoes de retorno
    def select_one(self, filter, returnOptions) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filter, returnOptions)
        return response
    #selecionando registros se determinada propriedade existir
    def select_if_property_exists(self) ->None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"user":{"$exists": True}})
        for element in data:
            print(element)
    #ordenando o retorno do bd
    def select_manyOrdered(self) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            {"listaDesejos.modelo":"Dunk Low", "listaDesejos.precoDesejado":550},
            {"_id":0, "user":1, "listaDesejos.categoria":1}
        ).sort([("user", -1)]) #-1 ordena de forma decrescente, 1 ordena de forma crescente   

       
        for element in data:
            print(element)
    
    #selecao de contatos para o nosso caso
    def select_contact(self, filter, returnOptions) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filter, returnOptions)

        contacts = []
        for element in data:
           contacts.append(int(element["user"]))
                        
        return contacts
    #seleçao para o filtro or
    def select_or_filter(self) ->None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"$or":[{"listaDesejos.modelo":"Dunk Low"}, {"ola": {"$exists":True}}]})
        for element in data:
            print(element)

    #editar registros da colecao
    def edit_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one({"name": "Diogo"},{"$set":{"name":"Diogo Cardinot"}}) #filtro, edição
        print(data.modified_count)#printa quantos elementos foram modificados
        
    #editar varios registros ao mesmo tempo
    def edit_many_registries(self,filtro, propriedades) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(filtro, {"$set":propriedades}) #filtro, edição
        print(data.modified_count)#printa quantos elementos foram modificados
    #incrementar valor a algum campo numérico
    def edit_many_increment(self, num) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many({"name": "Diogo"}, {"$inc": {"idade":num}}) #filtro, edição
        print(data.modified_count)#printa quantos elementos foram modificados

    def delete_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many({"name": "Diogo", "profissao": "Estudante"}) #filtro many or one para uma deleção só
        print(data.deleted_count)#printa quantos elementos foram modificados

    
    