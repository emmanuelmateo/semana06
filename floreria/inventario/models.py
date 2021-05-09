from django.db import models

# Create your models here.


class AlmacenModel(models.Model)


# aca iran todas las columnas en forma de atributos de la clase
almacenId = models.AutoField(
    unique=True,
    primary_key=True,
    null=False,
    db_column="id",  # para que su nombre de la columna en la bd sea diferente al del atributo
    verbose_name="Id del almacen",

)  # le indicamos que el atributos id sera un campor entero y autoincrementable. NOTA: solamente puede haber un autoincrementable por modelo( no puede haber mas de uno)
almacenNombre = model.CharField(
    max_length=30,  # parametro obligatorio para cuando sea charfield
    db_column="nombre",
    verbose_name="Nombre del almacen",
    # es un campo de ayuda que nos brinda una mejor información en el panel administrativo
    help_text="Nombrecito del almacen",
)
almacenDireccion = models.TextField(
    db_column="direccion",
    # NOTA: solamente usar verbose_name, help_text para cuando vayamos a utilizar el panel administrativo, caso contrario su uso es nulo
    verbose_name="Direccion almacen",
    help_text="Direccion expresada en texto indicando Calle Numero, Distrito, Provincia"
)
almacenEstado = models.BooleanField(
    # para indicar un valor por defecto en caso el cliente (frontend) no me lo diese y evitar que esa columna quede con un valor vacio
    default=True,
    null=False,
    db_column="estado",
    verbose_name="Estado del almacen",
    help_text="Estado de disponibilidad del almacen",
)


class Meta:
    # la clase meta es una clase propia de la clase en python y sirve para pasar metadatos(configuraciones adicionales) a la clase en la cual se esta haciendo la herencia ( en este caso estamos heredando de la clase Model)
    # por ejemplo para cambiar el nombre de la tabla en la bd:
    db_table = "almacenes"
    # para cuando querramos leer la información de la bd que nos devuelva en un orden específico, en este caso le estamos diciendo que retorne ordenado por la columna nombre en form DESC
    ordering = ["-nombre", ]
    # sirve para hacer que dos o mas columnas no se pueda repetir su misma información de todas esas columnas juntas
    unique_together = [["nombre", "direccion"], ["direccion", "estado"]]
    # validacion 1:
    # Almacen A | Calle juanes 123 ✅
    # Almacen A | Calle juanes 123 ❌
    # Almacen A | Calle chinchuli 345 ✅
    # Almacen B | Calle juanes 123 ✅
    # validacion 2:
    # Calle juanes 123 | true ✅
    # Calle juanes 123 | true ❌
    # Calle juanes 123 | false ✅
    # Calle achiote 123 | true ✅
    # ! NOTA: Los siguientes campos son para el panel administrativo:
    # se vera en el listado de los modelos en el panel administrativo
    verbose_name = "almacen"
    # se vera en el listado pero de una manera plural ya que puede contener varios registros
    verbose_name_plural = "almacenes"
