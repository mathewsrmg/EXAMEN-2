from clases.claseciclista import Ciclista

pkj = Ciclista()
ciclistas=[]
timers=[]

print("                        TRIATLON DE CICLISTAS")
print("")
print("                           $******.     .******")
print("               d$$$$$$$P                   $    ")
print("                   ^                     4r ")
print("                  d \                   //O  ")
print("                 P   \                //  \   ")
print("        ..ec.. .      \              //    \ asdasd..")
print("    .^        3*b.     \            // .@             4")
print("  .          d   ^b.    \       .  //  d                3")
print("4        .eE........$r=============// J       *..        b")
print("$       $$$$$       $   4=== ====     F       d$$$.      4")
print("$       $$$$$       $   4=== ====     L      *$$$        4")
print("4                  3P   =========     3                  P")
print(" *                 $                   b                 J ")
print("   .             .P                     %.             @")
print("    %.         z*                         ^%.       .r ")
print("        *==*                                    *=*  ")

print("--       seleccione para ingresar al programa (0)")
print("--       seleccione para salir del programa   (1)")
x = input()
if(x == "0"):
    while(True):
        print(" ")
        print("----------------------------------------------")
        print("---- 1.      Ingresar ciclista")
        print("---- 2.      Terminar")
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
            print(f"        no ingresaste mas ciclistas")
            break
elif(x == "1"):
    print("----------------------------------------------")
    print("gracias por usar nuestros servicios hasta luego.")
    print("----------------------------------------------")
else:
    print(f"No has digitado una opcion valida.")
    

print(ciclistas)
mejorTiempo = min(timers)
print(f'¡¡¡El cilista con mejor tiempo fue ')



#print(next(x for x in ciclistas if x['tiempo'] == mejorTiempo))
for ciclista in ciclistas:
    if (ciclista['tiempo']==mejorTiempo):
      print(f'El cilista con mejor tiempo fue de {ciclista["tiempo"]} el increible persona ¡{ciclista["nombre"]}! de nada mas y nada menos que ¡{ciclista["edad"]}! años de edad')
      print(f'del increible equipo de ¡{ciclista["equipo"]}! del pais que deberian estar orgullosos nada mas y nada menos que !{ciclista["pais"]}!!!')
#print(f'¡¡¡El cilista con mejor tiempo fue de {mejorTiempo} minutos la increible persona ¡{pkj.nombre}! de nada mas y nada menos que ¡{pkj.edad}! años de edad')
#print(f'del increible equipo de ¡{pkj.equipo}! del pais que deberian estar orgullosos nada mas y nada menos que !{pkj.pais}!!!')

#def consultarCiclista(nombre,edad,equipo,pais,tiempo):
#    for pkj in ciclistas:
#        if min(timers) == pkj.tiempo:
#            print (pkj.nombre, "-", pkj.edad)
            
#consultarCiclista()


