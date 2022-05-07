class Ciclista:
    def __init__(self):
        self.__name: None
        self.__age: None
        self.__country: None
        self.__team: None
        self.__time: None

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @property
    def country(self):
        return self.__country
    @property
    def team(self):
        return self.__team
    @property
    def time(self):
        return self.__time

    @name.setter
    def name(self,name):
        self.name = input("Digita el nombre del ciclista: ")

    @age.setter
    def age(self,age):
        if(age < 18):
            print("la edad digitada no es de un ciclista")
        else:
            self.age = int(input("Digita la edad del ciclista: "))

    @country.setter
    def country(self,country):
        self.country = input("Digita el pais del ciclista: ")

    @team.setter
    def team(self,team):
        self.team = input("Digita el equipo del ciclista: ")

    @time.setter
    def time(self,time):
        if(time < 0):
            print("el ciclista no es flash")
        else:
            self.time = input("Tiempo del ciclista:")


