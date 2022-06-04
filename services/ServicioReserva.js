import {modeloReserva} from '../models/reservaModelo.js'

export class ServicioReserva{

    constructor(){}

    async registrar(reserva){
        let reservaRegistrar=new modeloReserva(reserva)
        return await reservaRegistrar.save()
    }

    async buscarPorId(id){
        let reserva=await modeloReserva.findById(id)
        return reserva
    }

    async editar(id,datosPeticion){ 
        return await modeloReserva.findByIdAndUpdate(id,datosPeticion)
    }

    async eliminar(id){
        return await modeloReserva.findByIdAndDelete(id)
    }

}