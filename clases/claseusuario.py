class Usuario:
    def __init__(self):
        self.__nombre=None
        self.__apellido=None
        self.__cedula=None
        self.__ciudad=None
        
    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
        return self.__apellido
    @property
    def cedula(self):
        return self.__cedula 
    @property
    def ciudad(self):
        return self.__ciudad
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=input("Digite el nombre: ")
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido=input("Digite el apellido: ")
    @cedula.setter
    def cedula(self,cedula):
        self.__cedula=int(input("Digite la cedula: "))
    @ciudad.setter
    def ciudad(self,ciudad):
        self.__ciudad=input("Digita la ciudad: ")
