#from Materias.jsonMateria import crearjson
from jsonDatosSensor import  crearjson




class DatosSensor(crearjson):
    def __init__(self,nombre="", datos =0, fecha="",medida="",invernadero="",detalles=list()):
        super(DatosSensor, self).__init__('json/jsonDatosSensor.json')
        self.nombre = nombre
        self.datos = datos
        self.fecha = fecha
        self.medida = medida
        self.detalles = detalles
        self.invernadero = invernadero

        self.lista = list()

    def add(self, DatosSensor):
        self.lista.append(DatosSensor)

    def eliminar(self, DatosSensor):
        self.lista.remove(DatosSensor)

    def getMateria(self, index):
        return self.lista[index]

    def modificar(self, index, DatosSensor):
        self.lista[index] = DatosSensor

    def getlist(self):
        return self.lista

    def __str__(self):
        return self.nombre.ljust(20)

    def toObjects(self):
        lista = list()
        data = self.getDataJson()
        for x in data:
            lista.append(DatosSensor(nombre=x["nombre"],datos=x['datos'],medida=x['medida'],fecha=x['fecha'],detalles=x['detalles'],invernadero=x['invernadero']))
        self.lista = lista

    def getDictory(self):
        return {
            "nombre":self.nombre,
            "Datos Sensor": self.datos,
            "medida":self.medida,
            "fecha":self.fecha,
            "detalles": self.detalles,
            "invernadero": self.invernadero,


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
