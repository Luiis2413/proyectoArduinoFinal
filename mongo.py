import pymongo


import json

import os


class MongoConexion:
    def __init__(self, url, db_name, collection_name):
        self.url = url
        self.db_name = db_name
        self.collection_name = collection_name
        self.data = []

    def conect(self):
        try:
            self.client = pymongo.MongoClient(self.url)
            print("Conexion exitosa")
            return self.client
        except Exception as e:
            print("Error en conexion")

    def insert_one(self, data):

            client = pymongo.MongoClient(self.url)
            db = client[self.db_name]
            collection = db[self.collection_name]
            collection.insert_one(

                {
                    "filename": "jsonSensores.json",
                    "nombreSensor": data.nombreSensor,
                    "pines": data.pines,
                    "tipo": data.tipo,
                    "descr": data.descr,
                    "lista": []
                }
                                    )

    def insert_oneD(self, data):
                client = pymongo.MongoClient(self.url)
                db = client[self.db_name]
                collection = db[self.collection_name]
                collection.insert_one(

                    {
                        "filename": "jsonDatosSensores.json",
                        "nombre":data.nombre,
                        "datos": data.datos,
                        "medida": data.medida,
                        "fecha": data.fecha,
                        "lista": []
                    }
                )


            # si había datos en el archivo JSON, los sube a MongoDB


    def find_one(self, collection, query={}):
        coll = self.db[collection]
        return coll.find_one(query)

    def find_many(self, collection, query={}):
        coll = self.db[collection]
        return coll.find(query)

    def update_one(self, collection, query, new_values):
        coll = self.db[collection]
        coll.update_one(query, {"$set": new_values})

    def delete_one(self, collection, query):
        coll = self.db[collection]
        coll.delete_one(query)

    def delete_documents(self, collection, criteria):
        result = collection.delete_many(criteria)
        print("Se han eliminado {} documentos".format(result.deleted_count))

    def delete_many(self,):
        client = pymongo.MongoClient(self.url)
        db = client[self.db_name]
        collection = db[self.collection_name]
        collection.delete_many({})



ta = []