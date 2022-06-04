import {ServicioReserva} from '../services/ServicioReserva.js'
import {ServicioHabitacion} from '../services/ServicioHabitacion.js'

export class ControladorReserva{

    constructor(){}

    async buscarPorId(request,response){

        let servicioReserva=new ServicioReserva()
        let id=request.params.id
        console.log(id)
        try{
            response.status(200).json({
                mensaje:"Exito en la busqueda por id: "+id,
                data:await servicioReserva.buscarPorId(id),
                estado:true
            })
        }catch(error){
            response.status(400).json({
                mensaje:"Error buscando por id"+error,
                data:[],
                estado:false
            })
        }
    }

    async insertar(request,response){
        let servicioReserva=new ServicioReserva()
        let ServicioHabitacion=new ServicioHabitacion()

        let datosPeticion=request.body//Datos de la reserva(OBJETO)
        console.log(datosPeticion)
        try{
            
            //consultar cuanto vale por noche una habitacion?
            let habitacionConsultar=await ServicioHabitacion.buscarPorId(datosPeticion.idHabitacion)
            let percioNoche=habitacionConsultar.precio
            
            //fecha entrada
            let fechaEntrada=datosPeticion.fecha_in
            //fecha salida
            let fechaSalida=datosPeticion.fecha_out

            //Restar las fechas (Entrada-Salida)
            let diasTotales=fechaEntrada-fechaSalida
            
            //costo total de la reserva
            let costo= diasTotales*percioNoche

            datosPeticion.costo = costo

            await servicioReserva.registrar(datosPeticion)
            response.status(200).json({
                mensaje:"Exito agregando la reserva",
                data:datosPeticion,
                estado:true
            })
        }catch(error){
            response.status(400).json({
                mensaje:"Error agregando la reserva"+error,
                data:[],
                estado:false
            })
        }
    }

    async editar(request,response){
        let servicioReserva=new ServicioReserva()
        let id=request.params.id
        let datosPeticion=request.body
        try{
            await servicioReserva.editar(id,datosPeticion)
            response.status(200).json({
                mensaje:"Exito editando datos",
                data:null,
                estado:true
            })
        }catch(error){
            response.status(400).json({
                mensaje:"Error editando la reserva"+error,
                data:[],
                estado:false
            })
        }
    }

    async eliminar(request,response){
        let servicioReserva=new ServicioReserva()
        let id=request.params.id
        try{
            await servicioReserva.eliminar(id)
            response.status(200).json({
                mensaje:"Exito eliminando la reserva",
                data:null,
                estado:true
            })
    
        }catch(error){
            response.status(400).json({
                mensaje:"Error eliminando la reserva"+error,
                data:[],
                estado:false
            })
        }
    }
}