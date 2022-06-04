//Importo mongoose encargadod e crear la conexion
import mongoose from 'mongoose'

export async function conectar(){
    try{
        await mongoose.connect(process.env.DATABASE);
        console.log("Exito conectandonos con BD")

    }catch(error){
        console.log("Fallamos en la conexion con BD "+error)

    }
}