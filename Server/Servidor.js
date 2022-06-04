//Importaciones neecesarias:

//Importando express
import express from 'express'

//Importando las RUTAS
import {rutas} from '../routes/rutas.js'

//Importar la funcion de conexion
import {conectar} from '../database/conexion.js'

//PROGRAMO LA CLASE Servidor
export class Servidor{

    constructor(){

        this.app = express() //atributo app
        this.conectarConBD()
        this.llamarAuxiliares()
        this.enrutarPeticiones()

    }

    //METODOS DEL SERVIDOR (¿QUÉ HACE?)
    despertarServidor(){

        this.app.listen(process.env.PORT,function(){
            console.log("Servidor encendido")
        })

    }

    enrutarPeticiones(){
       this.app.use('/',rutas)  
    }

    llamarAuxiliares(){
        this.app.use(express.json())
    }

    conectarConBD(){
        conectar()
    }



}