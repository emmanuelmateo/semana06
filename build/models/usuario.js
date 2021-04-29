"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var _sequelize = require("sequelize");

var _sequelize2 = require("../config/sequelize");

var _bcrypt = require("bcrypt");

var _jsonwebtoken = require("jsonwebtoken");

//para poder utilizar las variables declaradas en el archivo .env , en este archivo debemos declarar lo siguiente
require("dotenv").config();

// Para ver las validaciones disponibles => https://sequelize.org/master/manual/validations-and-constraints.html#per-attribute-validations
var _default = () => {
  let usuario = _sequelize2.conexion.define("usuario", {
    usuarioId: {
      field: "id",
      type: _sequelize.DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
      unique: true
    },
    usuarioNombre: {
      field: "nombre",
      type: _sequelize.DataTypes.STRING(25)
    },
    usuarioApellido: {
      field: "apellido",
      type: _sequelize.DataTypes.STRING(25)
    },
    usuarioCorreo: {
      field: "correo",
      type: _sequelize.DataTypes.STRING(25),
      validate: {
        isEmail: true
      }
    },
    usuarioPassword: {
      field: "password",
      type: _sequelize.DataTypes.TEXT
    }
  }, {
    tableName: "usuarios",
    timestamps: false
  });
  /**Aqui ira la encriptación y algunos otros modelos PROPIOS DEL MODELO */


  usuario.prototype.setearPassword = function (password) {
    const hash = (0, _bcrypt.hashSync)(password, 10);
    this.usuarioPassword = hash; //console.log(hash);
  };

  usuario.prototype.validarPassword = function (password) {
    return (0, _bcrypt.compareSync)(password, this.usuarioPassword);
  };

  usuario.prototype.generarJWT = function () {
    const payload = {
      usuario: this.usuarioId,
      usuarioCorreo: this.usuarioCorreo
    }; // const password = "password";
    //return sign(payload, password, { expiresIn: "1h" });

    return (0, _jsonwebtoken.sign)(payload, process.env.JWT_SECRET, {
      expiresIn: "1h"
    });
  };

  return usuario;
};

exports.default = _default;