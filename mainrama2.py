from clases.clasecuenta import Cuenta   
from clases.claseusuario import Usuario
usuario= Usuario()
usuarios=[]
cuenta= Cuenta()
cuentas=[]

while(True):
    print("             CAJERO BANCO DE HIERRO DE")
    print("                  LA ISLA BRAVOS.")
    print("-- transaccion digite 0 para agregar cuenta")
    print("-- transaccion digite 1 para consultar cuenta")
    print("-- transaccion digite 2 para ingresar valor")
    print("-- transaccion digite 3 para retirar valor")
    x = input()
    if(x == "0"):
        while(True):
            cuenta.numero=0
            cuenta.saldo=0
            usuario.nombre=""
            usuario.apellido=""
            usuario.cedula=0
            usuario.ciudad=""
            cuentas.append({"cuenta":cuenta.numero,"saldo":cuenta.saldo})
            usuarios.append({"nombre":usuario.nombre,"apellido":usuario.apellido,"nit":usuario.cedula,"ciudad":usuario.ciudad})
            break
    elif(x == "1"):
        encontrarCuenta = int(input('Coloque la cuenta: '))
        print(next(x for x in cuentas if x['cuenta'] == encontrarCuenta))
        input("")
    elif(x == "2"):
        ingresarCuenta = int(input('Ingrese la cuenta a agregar saldo: '))
        print(next(x for x in cuentas if x['cuenta'] == ingresarCuenta))
        val2=int(input("Agregar saldo a la cartera: "))
 ##aqui esta la clave para traer el dato y convertirlo en int //cuenta.saldo = cuentas['saldo'] + val2
        print(cuenta.saldo) 

    elif(x == "3"):
        retirarCuenta = int(input('Ingrese la cuenta a retirar: '))
        print(next(x for x in cuentas if x['cuenta'] == retirarCuenta))
        print(next(x for x in cuentas if x['saldo'] == retirarCuenta))
        input("retirar saldo de la cartera")
#        retiro=int(input("cuanto es el dinero que desea retirar?: "))
#        if(retiro > saldoCuenta):
#                    print("El monto de retiro es mayor que el saldo")
#                else:    
#                    saldoCuenta = saldoCuenta-retiro
#                    print(f"total: {saldoCuenta}")
    else:
        print(f"No has digitado una opcion valida.")