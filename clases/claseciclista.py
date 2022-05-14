class Ciclista:
    def init(self):
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
        self.__nombre=input("set the nombre using setter: ")
    @edad.setter
    def edad(self,edad):
        self.__edad=int(input("set the edad using setter: "))
    @equipo.setter
    def equipo(self,equipo):
        self.__equipo=input("set the equipo using setter: ")
    @pais.setter
    def pais(self,pais):
        self.__pais=input("set the pais using setter: ")
    @tiempo.setter
    def tiempo(self,tiempo):
        self.__tiempo=int(input("set the tiempo using setter: "))



    


