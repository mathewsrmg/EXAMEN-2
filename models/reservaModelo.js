import mongoose from 'mongoose'

const Schema=mongoose.Schema

const Reserva=new Schema({

    idHabitacion:{
        type:String,
        requierd:true
    },

    nombre:{
        type:String,
        required:true
    },

    apellido:{
        type:String,
        required:true
    },

    telefono:{
        type:String,
        required:true
    },

    fecha_in:{
        type:Date,
        required:true
    },

    fecha_out:{
        type:Date,
        required:true
    },

    fecha_out:{
        type:Date,
        required:true
    },

    numero_personas:{
        type:Number,
        required:true
    },

    costo:{
        type:Number,
        requierd:false
    }
})

export const modeloReserva=mongoose.model('reservas',Reserva)