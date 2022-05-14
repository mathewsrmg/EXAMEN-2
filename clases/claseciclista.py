class Ciclista:
    def __init__(self):
        self.__nombre=None
        self.__edad=None
        self.__equipo=None
        self.__pais=None
        self.__tiempo=None
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @property
    def equipo(self):
        return self.__equipo
    @property
    def pais(self):
        return self.__pais
    @property
    def tiempo(self):
        return self.__tiempo 
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=input("Digite el nombre del ciclista: ")
    @edad.setter
    def edad(self,edad):
        self.__edad=int(input("Digite la edad del ciclista: "))
    @pais.setter
    def pais(self,pais):
        self.__pais=input("Digite el pais del ciclista: ")
    @equipo.setter
    def equipo(self,equipo):
        self.__equipo=input("Digite el equipo del ciclista: ")
    @tiempo.setter
    def tiempo(self,tiempo):
        self.__tiempo=int(input("Digite el tiempo del ciclista: "))

        




    


