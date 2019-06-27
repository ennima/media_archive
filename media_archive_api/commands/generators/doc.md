# Model Generator
Es un script que ayuda a programar APIs con Nodejs.

## Requerimientos
- Python 3

## ¿Cómo lo hace?
El script lee un archivo JSON de schemas en el cual se describen las tablas con las que un proyecto va a interactuar.

El script crear funciones CRUD dentro de un archivo javascript que funcionará como capa de interacción con la base de datos.

Crear funciones CRUD suele consumir tiempo y energía al desarrollar un API. Gracias a Model Generator es posible enfocarse en el desarrollo de las reglas de negocio. 

**Schemas(JSON) - - - >Build - - - > models.js**

## ¿Cómo usarlo?
Se debe crear un JSON con un array de schemas.

### Schema keys

#### name
Es el nombre de la tabla en MySQL
**Ejemplo:** `"name":"media_archive.transactions"`

- - -

#### object
Es el nombre del objeto representado por el schema, debe redactarse en singular y con la primera letra en mayúscula. Sin espacios.
**Ejemplo:** `"object":"Transaction",`

- - -

#### cols
Es un array con los nombres de los campos de la tabla.
**Ejemplo:** `"cols":["transaction_uid","clip_uid"]`


- - -

#### functions
Aquí se describen las funciones que se desean crear para dicho schema.
La sintaxis para describir dichas funciones es:
`<nombre_tipo_func>:<alias_en_código>`

##### Tipos de funciones

##### **list**
Entrega una lista de los registros dentro de la tabla.

##### **remove**
Elimina un ítem de la tabla

##### **update**
Actualiza los valores de una fila en la tabla.

##### **updatecol**
Actualiza solamente un valor de la fila.

##### **insert**
Agrega un elemento a la tabla

##### **count**
Entrega un entero con la cantidad de elementos en la tabla

##### **find**
Realiza una búsqueda dentro de la tabla tomado el campo Id como criterio de búsqueda.


#### built
Muchas veces habrá que añadir más schemas al proyecto. Quizá necesitaremos indicar que no vuelva a compilar algunos schemas. Pará ello basta con agregar la propiedad built.

Los schemas con built serán omitidos por el generador.

[Ejemplo de archivo schemas](/doc/schemas_example.json)