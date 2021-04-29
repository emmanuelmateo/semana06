import { Router } from "express";
import * as usuario_controller from "../controllers/usuario";

//import usuario from "../models/usuario";

export const usuario_router = Router();

usuario_router.post("/registro", usuario_controller.registro);
usuario_router.post("/login", usuario_controller.login);