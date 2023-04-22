#from Materias.jsonMateria import crearjson
from jsonSensor import  crearjson


class Sensor(crearjson):
    def __init__(self, nombreSensor='',pines="",tipo='',descripcion='',invernadero=''):
        super(Sensor, self).__init__('json/jsonMaterias.json')
        self.nombreSensor = nombreSensor
        self.pines=pines
        self.tipo=tipo
        self.invernadero=invernadero
        self.descr = descripcion

        self.lista = list()

    def add(self, Sensor):
        self.lista.append(Sensor)

    def eliminar(self, Sensor):
        self.lista.remove(Sensor)

    def getMateria(self, index):
        return self.lista[index]

    def modificar(self, index, Sensor):
        self.lista[index] = Sensor

    def getlist(self):
        return self.lista

    def __str__(self):
        return self.nombreSensor.ljust(20)

    def toObjects(self):
        lista = list()
        data = self.getDataJson()
        for x in data:
            lista.append(Sensor(nombreSensor=x['nombreSensor'],pines=x['pines'],tipo=x['tipo'],descripcion=x['descr'],invernadero=x['invernadero']))
        self.lista = lista

    def getDictory(self):
        return {
            "Nombre Sensor": self.nombreSensor,
            "pines":self.pines,
            "tipo":self.tipo,
            "descripcion":self.descr,
            "invernadero":self.invernadero
        }

    def __iter__(self):
        self.__idx__ = 0
        return self

    def __next__(self):
        if self.__idx__ < len(self.lista):
            x = self.lista[self.__idx__]
            self.__idx__ += 1
            return x
        else:
            raise StopIteration
