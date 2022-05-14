from clases.claseciclista import Ciclista

pkj = Ciclista()
ciclistas=[]
timers=[]

print("ciclistas")
print("-- seleccione para ingresar  (0)")
print("-- seleccione para salir del programa  (1)")
x = input()
if(x == "0"):
    while(True):
        print(" ")
        print("----------------------------------------------")
        print("---- 1. Ingresar ciclista")
        print("---- 2. Terminar")
        m = input()
        if(m == "1"):
            pkj.nombre = ""
            pkj.edad = 0
            pkj.equipo = ""
            pkj.pais = ""
            pkj.tiempo = 0
            ciclistas.append({"nombre":pkj.nombre,"edad":pkj.edad,"equipo":pkj.equipo,"pais":pkj.pais,"tiempo":pkj.tiempo})
            timers.append(pkj.tiempo)
        else:
            print(f"no ingresaste mas ciclistas")
            break
elif(x == "1"):
    print("----------------------------------------------")
    print("gracias por usar nuestros servicios hasta luego.")
    print("----------------------------------------------")
else:
    print(f"No has digitado una opcion valida.")
    
ciclistas 
print(ciclistas)
mejorTiempo = min(timers)
next(x for x in ciclistas if x['tiempo'] == mejorTiempo)

print(f'¡¡¡El cilista con mejor tiempo fue de {mejorTiempo} minutos la increible persona ¡{pkj.nombre}! de nada mas y nada menos que ¡{pkj.edad}! años de edad')
print(f'del increible equipo de ¡{pkj.equipo}! del pais que deberian estar orgullosos nada mas y nada menos que !{pkj.pais}!!!')

#def consultarCiclista(nombre,edad,equipo,pais,tiempo):
#    for pkj in ciclistas:
#        if min(timers) == pkj.tiempo:
#            print (pkj.nombre, "-", pkj.edad)
            
#consultarCiclista()


