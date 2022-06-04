//Importan los servicios
import {ServicioHabitacion} from '../services/ServicioHabitacion.js'

export class ControladorHabitacion{

    constructor(){}

    async buscarTodos(request,response){
        let serviciohabitacion=new ServicioHabitacion( )// Se instancia la clase SERVICIO
        try{

            response.status(200).json({
                mensaje:"Exito en la busqueda de todos",
                data:await serviciohabitacion.buscarTodos(),
                estado:true
            })
    
        }catch(error){
    
            response.status(400).json({
                mensaje:"Error en busqueda"+error,
                data:[],
                estado:false
            })
    
        }
    }

    async buscarPorId(request,response){
        let id=request.params.id //CAPTURO EL ID QUE LLEGA POR LA URL
        console.log("El id solicitado es: "+id)
        let serviciohabitacion=new ServicioHabitacion( )// Se instancia la clase SERVICIO
        try{

            response.status(200).json({
                mensaje:"Exito en la busqueda por id: "+id,
                data:await serviciohabitacion.buscarPorId(id),
                estado:true
            })
    
        }catch(error){
    
            response.status(400).json({
                mensaje:"Error editando por id"+error,
                data:[],
                estado:false
            })
    
        }
    }

    async insertar(request,response){
        let datosPeticion=request.body
        console.log(datosPeticion)
        let serviciohabitacion=new ServicioHabitacion( )// Se instancia la clase SERVICIO
        try{
            await serviciohabitacion.registrar(datosPeticion)
            response.status(200).json({
                mensaje:"Exito registrando datos",
                data:datosPeticion,
                estado:true
            })
    
        }catch(error){
    
            response.status(400).json({
                mensaje:"Error registrando los datos"+error,
                data:[],
                estado:false
            })
    
        }
    }

    async editar(request,response){
        let id=request.params.id
        let datosPeticion=request.body
        let serviciohabitacion=new ServicioHabitacion( )// Se instancia la clase SERVICIO
        try{
            await serviciohabitacion.editar(id,datosPeticion)
            response.status(200).json({
                mensaje:"Exito editando datos",
                data:null,
                estado:true
            })
    
        }catch(error){
    
            response.status(400).json({
                mensaje:"Error editando los datos"+error,
                data:[],
                estado:false
            })
    
        }
    }


    async eliminar(request,response){
        let id=request.params.id
        let servicio=new ServicioHabitacion( )// Se instancia la clase SERVICIO

        try{
            await servicio.eliminar(id)
            response.status(200).json({
                mensaje:"Exito eliminando datos",
                data:null,
                estado:true
            })
    
        }catch(error){
    
            response.status(400).json({
                mensaje:"Error eliminando los datos"+error,
                data:[],
                estado:false
            })
    
        }
    }

}