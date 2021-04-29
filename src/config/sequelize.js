import { Sequelize } from "sequelize";

export const conexion = new Sequelize(
    "almacen",
    "root",
    "Alpha5000",
    {
        // tambien podes usar dialectos para pgadmin, sqlserver, sqlite3, mariadb, mysql
        dialect: "mysql",
        host: "127.0.0.1",
        port: 3306,
        timezone: "-05:00", //no funciona en SQLITE
        dialectOptions: {
            // sirve para que al momento de mostrar las fechas, automaticamente las convierta en string y no tener que hacer una conversión manual
            dateStrings: true,
        },
        //no muestra los comandos del mysql
        logging: false,
    });