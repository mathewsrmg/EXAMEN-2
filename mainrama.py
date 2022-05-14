from clases.claseciclista import Ciclista

ciclistas=[]

ciclistarapido=""
ciclistarapidoage=0
ciclistarapidocountry=""
ciclistarapidoteam=""
ciclistarapidotime=1000

while(True):
    ingreso=input("Por favor ingresar r para registrar un ciclista o f para finalizar --:-- ")
    if (ingreso == "r"):
        ciclista= Ciclista()
        print("")
        print("--------------------------------------")
        name=input("1. Digita el nombre del ciclista: ")
        ciclista.name= name
        while(True):
            age=input("2. Digita la edad del ciclista: ")
            if age.isnumeric():
                ciclista.age=int(age)
                break
            else:
                print(age+" No es una edad")
        country=input("3. Digita el pais del ciclista: ")
        ciclista.country=country
        team=input("4. Digita el equipo del ciclista: ")
        ciclista.team=team
        while(True):
            time=input("5. Ingrese el tiempo en minutos: ")
            if time.isnumeric():
                ciclista.time=int(time)
                break
            elif(time == "0"):
                print("flash o que? es hijo de usaim bolt?")
            elif(time > "1000"):
                print("la carrera no dura una eternidad...")
            else:
                print(time+" No es un tiempo")
        ciclistas.append({"nombre":ciclista.name,"edad":ciclista.age,"pais":ciclista.country,"equipo":ciclista.team,"tiempo":ciclista.time})
        if(ciclista.time<ciclistarapidotime):
            ciclistarapidotime=ciclista.time
            ciclistarapido=ciclista.name
            ciclistarapidoage=ciclista.age
            ciclistarapidocountry=ciclista.country
            ciclistarapidoteam=ciclista.team
        input("Se registro con exito el ciclista")
    elif(ingreso == "f"):
        break
    else:
        print("*error en la digitacion*")
        input("")
print(ciclistas)

print(f"¡El cilista mas rapido con {ciclistarapidotime} minutos es el inigualable {ciclistarapido} con una edad de {ciclistarapidoage}")
print(f"Del pais del que deberian estar con un gran orgullo {ciclistarapidocountry} del equipo {ciclistarapidoteam} es el ganador!")


