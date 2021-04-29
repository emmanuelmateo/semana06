import { Router } from "express";
import * as producto_controller from "../controllers/producto";
import producto from "../models/producto";

export const producto_router = Router();
producto_router.route("/productos")
    .post(producto_controller.crearProducto)
    .get(producto_controller.listarProductos);
