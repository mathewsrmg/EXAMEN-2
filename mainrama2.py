from clases.clasecuenta import Cuenta   
from clases.claseusuario import Usuario
import random

usuarios=[]
cuentas=[]

entrada = True
print("-------------------------------------------------------------")
print("        *          CAJERO BANCO DE HIERRO DE        *        ")
print("     *     *         LA ISLA BRAVOS S.A.S ©      *     *     ")
print("-------------------------------------------------------------")
while(entrada == True):
    print("                | • [0] AGREGAR CUENTA    • |")
    print("                | • [1] CONSULTAR CUENTA  • |")
    print("                | • [2] INGRESAR SALDO    • |")
    print("                | • [3] RETIRAR SALDO     • |")
    print("                | • [4] SALIR DEL CAJERO  • |")
    x = input("Digite una opción: ")
    if(x == "0"):
            cuenta= Cuenta()
            numero= random.randint(1, 100)
            cuenta.numero=numero 
            cuenta.saldo=0
            usuario= Usuario()
            usuario.nombre=""
            usuario.apellido=""
            usuario.cedula=""
            usuario.ciudad=""
            cuentas.append({"numero":cuenta.numero,"saldo":cuenta.saldo})
            usuarios.append({"nombre":usuario.nombre,"apellido":usuario.apellido,"nit":usuario.cedula,"ciudad":usuario.ciudad})
            print(f'-----El numero de la cuenta es: {numero}-----')
            input("pulsa una tecla para continuar")
    elif(x == "1"):
        encontrarCuenta = int(input('Coloque la cuenta: '))
        flag = True
        print(" ")
        for cuenta in cuentas:
            if cuenta['numero'] == encontrarCuenta:
                print("---------------| • INFORMACIÓN DE LA CUENTA  • |---------------")
                print("•numero de cuenta: " + str(cuenta['numero']))
                print("•saldo de la cuenta: " + str(cuenta['saldo']) + "$")
                flag = True
                break
            else:
                flag = False
        if(flag == False):        
            print('El numero de la cuenta es incorrecto')
        input("pulsa una tecla para continuar")
    elif(x == "2"):
        ingresarCuenta = int(input('Ingrese la cuenta a agregar saldo: '))
        sumaCuenta = int(input('Cantidad de saldo a agregar: '))
        flag = True
        print(" ")
        for cuenta in cuentas: 
            if cuenta['numero'] == ingresarCuenta:
                cuenta['saldo'] = cuenta['saldo'] + sumaCuenta
                print('Transacción realizada con exito.')
                flag = True
            else:
                flag = False
        if(flag == False):        
            print('El numero de la cuenta es incorrecto')
        input("pulsa una tecla para continuar")
    elif(x == "3"):
        retirarCuenta = int(input('Ingrese la cuenta a retirar: '))
        restaCuenta = int(input('Cantidad de saldo a retirar: '))
        flag = True
        print(" ")
        for cuenta in cuentas: 
            if cuenta['numero'] == retirarCuenta:
                if (cuenta['saldo'] < restaCuenta):
                    print('¡El monto de retiro no puede superar el saldo!.')
                else:
                    cuenta['saldo'] = cuenta['saldo'] - restaCuenta
                    print('Transacción realizada con exito.')
                    flag = True
            else:
                flag = False
        if(flag == False):        
            print('El numero de la cuenta es incorrecto')
        input("pulsa una tecla para continuar")
#        retiro=int(input("cuanto es el dinero que desea retirar?: "))
#        if(retiro > saldoCuenta):
#                    print("El monto de retiro es mayor que el saldo")
#                else:    
#                    saldoCuenta = saldoCuenta-retiro
#                    print(f"total: {saldoCuenta}")
    elif(x == "4"):
        print("Saliendo del cajero...")
        print("        --GRACIAS POR USAR EL SOFTWARE HASTA PRONTO--")
        entrada = False
    else:
        print(f"No has digitado una opcion valida.")