//libreria que nos permite manipular nuestro storage de firebase
import { Storage } from "@google-cloud/storage";
//inicializamos el objeto de firebase para poder conectarnos al almacenamiento(bucket)
const storage = new Storage({
    projectId: "codigoonline2mateo",
    keyFilename: "./credenciales_firebase.json"
});

//ahora creamos la instancia de nuestro storage
const bucket = storage.bucket("codigoonline2mateo.appspot.com")
export const subirArchivo = (archivo) => {
    //return new Promise((resolve,reject))
    return new Promise((resuelto, rechazo) => {
        //validamos que tengamos un archivo que subir
        if (!archivo) return rechazo("No se encontró el archivo");
        // definimos el nombre del archivo con el cual se guardará en firebase storage
        const file = bucket.file(archivo.originalname);
        //agregamos la configuración adicional de nuestro archivo como su extensión y formato
        const blobStream = file.createWriteStream({
            metadata: {
                contentType: archivo.mimetype,
            },
        });
        //el proceso de subida se genera en un segundo plano, mediante el cual se controla en estado
        blobStream.on("error", (error) => {
            //ingresara cuando el archivo tuvo problema para subirse a firebase
            return rechazo(error);
        });
        blobStream.on("finish", () => {
            //ingresará a este arrow function cuando el archivo termine de subir exitosamente
            //getSignedUrl sirve para que nos brinde firebase una ruta para acceder a nuestro archivo fuera del storage
            file.getSignedUrl({
                action: "read",
                expires: "12-31-2021", //MM-DD-YYYY
            }).then((link) => {
                return resuelto(link);
            })
                .catch((error) => {
                    return rechazo(error);
                })
        });
        //culmino el proceso de conexión firebase
        // le mando el contenido del archivo
        // en si este es el inicio y fin de la conexión con firebase, luego recien viene los estados de mas arriba
        blobStream.end(archivo.buffer);
    })
}

export const eliminarArchivo = (nombreArchivo) =>
    bucket.file(nombreArchivo).delete();

