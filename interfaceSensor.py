import mongo

from Sensor import Sensor
from datosSensor import DatosSensor

import os

import interfaceDatosArduino


interacciondb = mongo.MongoConexion("mongodb+srv://abel0120:01abel01@cluster0.mndru6r.mongodb.net/?retryWrites=true&w=majority", "sistemaSensores", "Sensores")

class InterfaceSensor():
    def __init__(self):
        self.datsen = DatosSensor()
        self.datsen.toObjects()
        self.lista = Sensor()
        self.lista.toObjects()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def nuevoDatoSensor(self):
        listaDataSEnsor = DatosSensor()

        listaDataSEnsor.nombre = ""
        listaDataSEnsor.medida = ""
        listaDataSEnsor.datos = 0
        listaDataSEnsor.detalles = []
        listaDataSEnsor.invernadero = "a"

        return listaDataSEnsor

    def nuevoSensor(self):

        listaSensor = Sensor()


        listaSensor.nombreSensor = input("Nombre del Sensor:")
        listaSensor.tipo = input("tipo de sensor:")
        cantPin=int(input("ingresa la cantidad de pines"))
        pines=list()
        i=0
        while i!= cantPin:
            p=input("pin:")
            pines.append(p)
            i=i+1
        listaSensor.pines=str(pines)
        listaSensor.descr=input("descripcion:")






        interacciondb.conect()
        if (interacciondb.conect()):
            interacciondb.insert_one(listaSensor)


        return listaSensor

    def mostrarSensor(self, lista=None):
        self.cls()
        print("\n\n" + "-" * 10 + "Datos de Sensor" + "" * 10)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'Nombre'.ljust(20)+'tipo'.ljust(20)+'pines')
        i = 0

        interacciondb.conect()
        if (interacciondb.conect()):
            interacciondb.delete_many()


        for listaSensor in mylista:
            print(str(i).ljust(5) + "\t\t" + listaSensor.nombreSensor+ "\t\t"+listaSensor.tipo +"\t\t"+listaSensor.pines+"\t\t"+listaSensor.descr)
            i += 1

            if (interacciondb.conect()):
                interacciondb.insert_one(listaSensor)


    def buscarSensor(self, code):
        mylista = [listaSensor for listaSensor in self.lista if listaSensor.nombreSensor == code]
        self.mostrarSensor(mylista)

    def getListaSensor(self):
        return self.lista

    def modificarSensor(self):
        id = input("Introduce ID:")
        id = int(id)
        listaSensor= self.lista.getlist()[id]
        cadena = input("Nombre del Sensor:")
        if (len(cadena) > 0):
            listaSensor.nombreSensor = cadena
            cadena = input("tipo de Sensor:")
        if (len(cadena) > 0):
            listaSensor.tipo = cadena

        cadena = input("numero de pines")
        if (len(cadena) > 0):
            cantPin=int(cadena)
            i = 0
            pines = list()

            while i != cantPin:
                p = input("pin:")
                pines.append(p)
                i = i + 1
            listaSensor.pines = str(pines)

        self.lista.modificar(id, listaSensor)

    def eliminarSensor(self):
        id = input("Introduce ID:")
        id = int(id)
        print(self.lista.getMateria(id))
        self.lista.eliminar(self.lista.getMateria(id))

        print("NO SE TE OLVIDE ELIMINAR LOS DATOS GUARDADOS EN EL MENU PRINCIIPAL, DATOS SENSOR !!")
        l=input("presiona Enter para continuar...")

    def menuSensor(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "-" * 10 + "Menum Sensores" + "-" * 10)
            print("1) Nueva Sensor\n2) Modificar Sensor\n3) Eliminar Sensor\n4) Mostrar Sensor\n0)salir")

            a = input("Selecciona una opción: ")
            if (a == '1'):
                p = self.nuevoSensor()
                self.lista.add(p)
                self.lista.toJson(self.lista)

                d= self.nuevoDatoSensor()
                self.datsen.add(d)
                self.datsen.toJson(self.datsen)


                print("REINICIE EL PROGRAMA ANTES DE LEER LOS DATOS!!")
                l = input("presiona Enter para continuar...")
            elif (a == '2'):
                self.mostrarSensor()
                self.modificarSensor()
                self.lista.toJson(self.lista)
            elif (a == '3'):
                self.mostrarSensor()
                self.eliminarSensor()
                self.lista.toJson(self.lista)

            elif (a == '4'):
                self.mostrarSensor()
            elif (a == '0'):
                break
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()