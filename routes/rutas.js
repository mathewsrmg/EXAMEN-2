import express from 'express'

import {ControladorHabitacion} from '../controllers/ControladorHabitacion.js'
import {ControladorReserva} from '../controllers/ControladorReserva.js'

let controladorHabitacion= new ControladorHabitacion()
let controladorReserva = new ControladorReserva()

export let rutas=express.Router()

rutas.get('/API/v1/viernes', controladorHabitacion.buscarTodos)
rutas.get('/API/v1/viernes/:id', controladorHabitacion.buscarPorId)
rutas.post('/API/v1/viernes', controladorHabitacion.insertar)
rutas.put('/API/v1/viernes/id', controladorHabitacion.editar)
rutas.delete('/API/v1/viernes/id', controladorHabitacion.eliminar)

rutas.get('/API/v1/reserva/:id', controladorReserva.buscarPorId)
rutas.post('/API/v1/reserva', controladorReserva.insertar)
rutas.put('/API/v1/reserva/id', controladorReserva.editar)
rutas.delete('/API/v1/reserva/id', controladorReserva.eliminar)