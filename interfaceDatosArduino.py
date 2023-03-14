import mongo
from os import remove
from datetime import datetime

from Sensor import Sensor
from datosSensor import DatosSensor
import os
import serial
import time


interacciondb = mongo.MongoConexion("mongodb://localhost:27017", "sistemaSensores", "DatosSensores")

class InterfaceDatosSensor():
    def __init__(self):
        self.listaS = Sensor()
        self.listaS.toObjects()
        self.lista = DatosSensor()
        self.lista.toObjects()
        self.puerto = ""

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def nuevoSensor(self):

        listaSensor = Sensor()
        listaSensor.nombreSensor = input("Nombre del Sensor:")
        listaSensor.tipo = input("tipo de sensor:")
        cantPin = int(input("ingresa la cantidad de pines"))
        pines = list()
        i = 0
        while i != cantPin:
            p = input("pin:")
            pines.append(p)
            i = i + 1
        listaSensor.pines = str(pines)
        listaSensor.descr = input("descripcion:")

        return listaSensor

    def mostrarSensor(self, lista=None):
        self.cls()
        print("\n\n" + "-" * 10 + "Datos de Sensor" + "" * 10)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("ID".ljust(5) +"\t\t" + 'nombre'.ljust(20)+ "\t\t" + 'Datos'.ljust(20)+'Fecha'.ljust(20)+'')
        i = 0




        for listaSensor in mylista:
            print(str(i).ljust(5) + "\t\t" + listaSensor.nombre+"\t\t" + str(listaSensor.datos) +  listaSensor.medida+ "\t\t"+listaSensor.fecha )
            i += 1




    def buscarSensor(self, code):
        mylista = [listaSensor for listaSensor in self.lista if listaSensor.datos == code]
        self.mostrarSensor(mylista)

    def getListaSensor(self):
        return self.lista

    def modificarSensor(self,listaS=None):
        self.cls()


        print(self.puerto)

        if (listaS == None):
            mylistaS = self.listaS
        else:
            mylistaS = listaS



        id = 0


        ser = serial.Serial(self.puerto, 9600)  # Reemplaza 'COM3' con el nombre del puerto serial del Arduino
        i=0
        for listaSensor in mylistaS:

            cadena = ser.readline()
            nom = cadena.decode('utf-8').rstrip()




            cadena = ser.readline()
            dats = cadena.decode('utf-8').rstrip()

            cadena = ser.readline()
            medida = cadena.decode('utf-8').rstrip()

            now = datetime.now()

            listaSensor = self.lista.getlist()[id]
            listaSensor.nombre = str(nom)
            listaSensor.datos = int(dats)
            listaSensor.medida = medida

            listaSensor.fecha = str(now)
            self.lista.modificar(id, listaSensor)

            if (interacciondb.conect()):
                interacciondb.insert_oneD(listaSensor)
            self.lista.toJson(self.lista)


            id=id+1
        # time.sleep(2)






        return listaSensor

    def eliminarSensor(self):
        id = input("Introduce ID:")
        id = int(id)
        print(self.lista.getMateria(id))
        self.lista.eliminar(self.lista.getMateria(id))

    def menuSensor(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "-" * 10 + "Menu Datos Sensor" + "-" * 10)
            print("1) leer datos\n2) Modificar datos Sensor\n3) Eliminar datos Sensor\n4) Mostrar datos Sensor\n0)salir")

            a = input("Selecciona una opción: ")
            if (a == '1'):
              """  p = self.nuevoSensor()
                self.lista.add(p)
                self.lista.toJson(self.lista)"""
              self.puerto=input("Escribe el puerto")
              while True:
                time.sleep(5)

                self.mostrarSensor()
                self.modificarSensor(None)



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