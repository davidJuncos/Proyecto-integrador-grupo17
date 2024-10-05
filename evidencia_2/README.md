# Proyecto-integrador-grupo3
 INTEGRANTES:
 <table style="width: 100%;">
  <tr>
   <th>
    NOMBRE
   </th>
   <th>
    APELLIDO
   </th>
   <th>
    DNI
   </th>
   <th>
    EMAIL
   </th>
   <th>
    REPOSITORIO GIT
   </th>
   <th>
    REPOSITORIO PERSONAL
   </th>
   <tr>
    <td>
     John
    </td>
    <td>
     Mackinson
    </td>
    <td>
     45.837.754
    </td>
    <td>
     john200430@gmail.com
    </td>
    <td>
      https://github.com/johnmack10
    </td>
    <td>
      https://github.com/johnmack10/repo_personal
    </td>
   </tr>
  <tr>
    <td>
     Tomás
    </td>
    <td>
     Ferrere
    </td>
    <td>
     44.762.329
    </td>
    <td>
     ferreretomas07@gmail.com
    </td>
    <td>
      https://github.com/ttomy14
    </td>
    <td>
      https://github.com/ttomy14/Repositorio_Personal
    </td>
   </tr>
  <tr>
    <td>
     David Eduardo
    </td>
   <td>
     Juncos
    </td>
    <td>
     29686787
    </td>
    <td>
     davidjuncos@hotmail.com
    </td>
    <td>
      https://github.com/davidJuncos
    </td>
    <td>
      https://github.com/davidJuncos/Personal-ISPC-Evidencia2
    </td>
   </tr>
  <tr>
  
   </tr>
  </tr>
  </th>
   <tr>
    <td>
    Cesia Fiorella 
    </td>
    <td>
     Cáceres Giménez
    </td>
    <td>
   96320512
    </td>
    <td>
    cesiaf.gimenez@gmail.com
    </td>
    <td>
     https://github.com/Cesiaf
    </td>
    <td>
      .
    </td>
   </tr>
   </th>
   <tr>

   </tr>
 </table>

 
# Evidencia N° 2 - Módulo Innovación en Gestión de Datos

## Descripción del Proyecto

Este proyecto consta de dos partes principales:

1. **Programación I (Python - POO y archivos binarios)**:
    - Implementación de las clases `Usuario` y `Acceso` en Python, siguiendo el paradigma de Programación Orientada a Objetos (POO).
    - Gestión del CRUD de usuarios, almacenamiento en un archivo binario (`usuarios.ispc`), y registro de accesos en otro archivo binario (`accesos.ispc`).
    - Control de accesos fallidos registrado en un archivo de texto (`logs.txt`).

2. **Base de Datos II (MySQL)**:
    - Creación de una base de datos relacional en MySQL con tablas y relaciones (PK y FK).
    - Inserción de datos en las tablas y realización de consultas SQL, incluyendo un CRUD y consultas con `JOIN`.

## Instrucciones de Ejecución

### Programación I

1. Asegurarse de tener instalado **Python 3.x** en el equipo.
2. Clonar el repositorio y navegar hasta la carpeta `evidencia2/Programacion`.
3. Ejecutar el archivo principal del programa para acceder al menú principal:
   ```bash
   python main.py
   ```
4. Desde el menú, se podrán realizar las siguientes acciones:
   - Agregar, modificar, eliminar y buscar usuarios.
   - Ingresar al sistema con un usuario existente (se verifica `username` y `password`).
   - Salir del programa.

5. Los archivos binarios `usuarios.ispc` y `accesos.ispc` serán generados automáticamente para almacenar los datos.

### Base de Datos II

1. Asegurarse de tener **MySQL Workbench** instalado y configurado en el sistema.
2. En la carpeta `evidencia2/BaseDeDatos` se encuentran tres archivos `.sql` que deben ejecutarse en el siguiente orden para configurar la base de datos correctamente:

   - **1. Estructura de la base de datos**: 
     Cargar el archivo `Gestion_hoteles_DB.sql`, que contiene las definiciones de las tablas y la creación del esquema de la base de datos, realizando lo siguiente:
     - En MySQL Workbench, hacer clic en **File** > **Open SQL Script** y seleccionar el archivo `Gestion_hoteles_DB.sql`.
     - Hacer clic en el botón **Execute** (ícono del rayo) para ejecutar el script y crear la estructura de la base de datos, incluyendo la creación del esquema `hoteles`.

   - **2. Inyección de datos**: 
     Cargar el archivo `insert_statements_hoteles.sql`, que contiene los datos que se insertarán en cada tabla:
     - En MySQL Workbench, ir a **File** > **Open SQL Script** y seleccionar el archivo `insert_statements_hoteles.sql`.
     - Ejecutar el script haciendo clic en el botón **Execute** para insertar los datos en las tablas correspondientes.

   - **3. Consultas y CRUD**: 
     Cargar el archivo `CRUD_queries_hoteles.sql`, que incluye el CRUD (select, insert, update, delete) y otras consultas SQL necesarias:
     - En MySQL Workbench, ir a **File** > **Open SQL Script** y seleccionar el archivo `CRUD_queries_hoteles.sql`.
     - Ejecutar el script haciendo clic en **Execute** para cargar las consultas que se utilizarán en el programa Python.

3. Al seguir este orden de ejecución, la base de datos quedará configurada con la estructura, los datos iniciales y las consultas necesarias para interactuar con el backend del programa realizado en Python.

## Explicación:
- El archivo Gestion_hoteles_DB.sql es el que crea la estructura de la base de datos (tablas y relaciones).
- El archivo insert_statements_hoteles.sql inserta los datos en las tablas.
- El archivo CRUD_queries_hoteles.sql contiene las consultas y el CRUD que se utilizarán para interactuar con la base de datos.

## Preguntas Frecuentes

- **¿Cómo ejecutar y probar este programa?**
   - Para la parte de programación, ejecutar el archivo `main.py` desde la carpeta `evidencia2`. Para la parte de bases de datos, utilizar **MySQL Workbench** para importar la estructura de la base de datos, inyectar los datos y ejecutar las consultas SQL proporcionadas, siguiendo el orden descrito anteriormente.

- **¿Qué inconvenientes se presentaron?**
   - Algunas dificultades incluyeron la serialización y deserialización correcta de objetos en archivos binarios en Python, así como el manejo de relaciones entre tablas en MySQL. Estos problemas se superaron mediante pruebas iterativas y ajustes en la lógica de la aplicación y en las consultas SQL.

- **¿Es necesario instalar algo adicional?**
   - Además de **Python**, se debe tener **MySQL Workbench** instalado para manejar la base de datos y ejecutar los scripts SQL de manera adecuada.

