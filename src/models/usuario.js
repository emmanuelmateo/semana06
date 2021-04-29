//para poder utilizar las variables declaradas en el archivo .env , en este archivo debemos declarar lo siguiente
require("dotenv").config();
import { DataTypes } from "sequelize";
import { conexion } from "../config/sequelize";
import { hashSync, compareSync } from 'bcrypt';
import { sign } from "jsonwebtoken";
// Para ver las validaciones disponibles => https://sequelize.org/master/manual/validations-and-constraints.html#per-attribute-validations
export default () => {
    let usuario = conexion.define(
        "usuario",
        {
            usuarioId: {
                field: "id",
                type: DataTypes.INTEGER,
                autoIncrement: true,
                primaryKey: true,
                unique: true,
            },
            usuarioNombre: {
                field: "nombre",
                type: DataTypes.STRING(25),
            },
            usuarioApellido: {
                field: "apellido",
                type: DataTypes.STRING(25),
            },
            usuarioCorreo: {
                field: "correo",
                type: DataTypes.STRING(25),
                validate: {
                    isEmail: true,
                },
            },
            usuarioPassword: {
                field: "password",
                type: DataTypes.TEXT,
            },
        },
        {
            tableName: "usuarios",
            timestamps: false,
        }
    );

    /**Aqui ira la encriptación y algunos otros modelos PROPIOS DEL MODELO */
    usuario.prototype.setearPassword = function (password) {
        const hash = hashSync(password, 10);
        this.usuarioPassword = hash;
        //console.log(hash);
    };

    usuario.prototype.validarPassword = function (password) {
        return compareSync(password, this.usuarioPassword);
    };

    usuario.prototype.generarJWT = function () {
        const payload = {
            usuario: this.usuarioId,
            usuarioCorreo: this.usuarioCorreo,
        };
        // const password = "password";
        //return sign(payload, password, { expiresIn: "1h" });
        return sign(payload, process.env.JWT_SECRET, { expiresIn: "1h" });
    };

    return usuario;
};


