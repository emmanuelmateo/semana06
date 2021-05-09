from django.db import models

# Create your models here.


class AlmacenModel(models.Model):
    # aca iran todas las columnas en forma de atributos de la clase
    almacenId = models.AutoField(
        unique=True,
        primary_key=True,
        null=False,
        db_column="id",  # para que su nombre de la columna en la bd sea diferente al del atributo
        verbose_name="Id del almacen",

    )  # le indicamos que el atributos id sera un campor entero y autoincrementable. NOTA: solamente puede haber un autoincrementable por modelo( no puede haber mas de uno)
    almacenNombre = models.CharField(
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
        ordering = ["-almacenNombre", ]
        # sirve para hacer que dos o mas columnas no se pueda repetir su misma información de todas esas columnas juntas
        unique_together = [["almacenNombre", "almacenDireccion"], [
            "almacenDireccion", "almacenEstado"]]
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


class ProductoModel(models.Model):
    productoId = models.AutoField(
        primary_key=True,
        null=False,
        unique=True,
        db_column="id"
    )

    productoNombre = models.CharField(
        max_length=50,  # parametro obligatorio para cuando sea charfield
        db_column="nombre",
        null=False,
        unique=True,
        verbose_name="Nombre del producto",
        # es un campo de ayuda que nos brinda una mejor información en el panel administrativo
        help_text="Nombrecito del producto",
    )
    productoDescripcion = models.CharField(
        max_length=100,
        db_column="descripcion",
        null=False,
        default="Por el momento no hay descripcion del producto",
        verbose_name="Descripcion del producto"
    )

    productoEstado = models.BooleanField(
        default=True,
        null=False,
        db_column="estado",
        verbose_name="Estado del producto"
    )
    productoPrecio = models.DecimalField(
        max_digits=5,  # para indicar cuantos numeros en total seran permitidos almacenar
        decimal_places=2,  # para indicar del total de numeros cuantos decimales se podran almacenar
        db_column="precio",
        null=False,
    )

    class Meta:
        db_table: "productos"
        verbose_name = "producto"
        verbose_name_plural = "productos"


# RELACIONES
almacenId = models.ForeignKey(
    to=AlmacenModel,
    # sirve para indicar que sucedera cuando un registro que hace referencia a una fk sea elimiando, y sus opciones son:
    # CASCADE = si la pk es eliminado todas sus referencias tambien seran eliminadas
    # PROTECT = no permitira la eliminación de la pk siempre y cuando tenga referencias
    # SET_NULL = si la pk es eliminada, sus referencias pasaran a un valor de NULL
    # DO_NOTHING = si la pk es eliminada, mantendra el mismo valor sus referencias, lo que ocasionara una mala integridad de los datos
    # RESTRICT = no permite la eliminacion de la pk y lanzara un error de tipo RestrictError
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey.on_delete
    on_delete=models.PROTECT,
    db_column="almacenes_id",
    # related_name = sirve para ingresar a su relacion inversa, es decir cuando querramos saber todos los productos que tinen un almacen específico, si no se otorga un nombre, django le pondra usando un formato establecido =  usara el nombre del modelo con el sufijo _set => almacen_set
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey.related_name
    related_name="almacenProductos"
)
