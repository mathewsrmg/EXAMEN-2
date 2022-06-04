//Importamos el modelo de datos
import {modeloHabitacion} from '../models/habitacionModelo.js'

export class ServicioHabitacion{

    constructor(){}

    
    async registrar(habitacion){
        let habitacionaRegistrar=new modeloHabitacion(habitacion)
        return(await habitacionaRegistrar.save())
    }

    async buscarTodos(){
        let habitaciones=await modeloHabitacion.find()
        return habitaciones
    }

    async buscarPorId(id){
        let habitacion=await modeloHabitacion.findById(id)
        return habitacion
    }

    async editar(id,habitacion){ 
        return(await modeloHabitacion.findByIdAndUpdate(id,habitacion))
    }

    async eliminar(id){
        return(await modeloHabitacion.findByIdAndDelete(id))
    }

}