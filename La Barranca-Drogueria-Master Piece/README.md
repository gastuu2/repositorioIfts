# Drogueria La Barranca

-A grandes rasgos, ¿cómo será el flujo del programa?

El flujo del programa contara principalmente con un logueo para verificar quien esta ingresando y se debe poder hacerlo, contara con un boton de registro para nuevos usuarios. Una vez dentro el usuario podra consultar todo lo referido a las ventas del negocio, tales como producto mas vendido, cliente con mas compras de productos y productos por clientes.


¿Qué estructura se utilizará para representar la información del archivo?

La informacion es alamcenada en un archivo csv con la siguiente estructura en columnas : CODIGO,CLIENTE,PRODUCTO,CANTIDAD,PRECIO



¿Cómo se usa el programa?
Primero se introduce la URL en el navegador para ingresar al sitio, una vez dentro se debe loguearse para obtener acceso a todas las funciones del sistema(si no se posee un usuario se debe registrar uno nuevo),una vez dentro se elije del menu de busqueda la busqueda que mas se ajusta las necesidades del momento, una vez finalizada la tarea que el usuario cree oportuna para la situacion dada en su caso particular se podra desloguear para mantener su privacidad intacta de manos ajenas y cochinas.



¿Qué clases se diseñaron?¿Por qué?

Se diseñaron las clases: "app.py","csv.validador.py","lista-clientes.py" y "forms.py"
app.py= es la clase principal que ejecuta la aplicacion e importa las demas requeridas.
csv.validador.py= valida que el archivo csv que se va a utilizar cumpla con las condiciones necesarias para ser leido
lista-clientes.py= contiene los metodos para realizar las distintas busquedas requeridas por el usuarios
forms.py= contiene todos los formularios usados en la aplicacion.


APP.PY: Contiene el main de la aplicacion

CONSULTAS.PY: Se encarga del manejo de todas las consultas de informacion a la base

VALIDADOR_ARCHIVO.PY: Se encarga de validar el formato de los campos y registros de las ventas.

FORMS.PY: Se encarga del manejo de los formularios usados a lo largo de toda la aplicacion
