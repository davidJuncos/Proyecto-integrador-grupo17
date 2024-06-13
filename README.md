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
 </table>
 

---

# SISTEMA GESTIÓN DE HOTEL
## DESCRIPCIÓN 

Este sistema de gestión de hotel integraría diversas funciones para facilitar la administración eficiente del establecimiento. Incluiría módulos para la gestión de habitaciones, clientes, reservas y empleados. Con respecto a las habitaciones, permitiría realizar un seguimiento de la disponibilidad, asignación y estado de las mismas. Para los clientes, registraría información personal e historial de reservas. En cuanto a las reservas, facilitaría la gestión de disponibilidad, confirmación, modificaciones y cancelaciones. Además, el sistema administraría datos de los empleados, como horarios y roles. En resumen, un sistema integral que optimiza la operación y la experiencia tanto para los huéspedes como para el personal del hotel.



# Detalle de Archivos Python en la Aplicación

* En crud_cliente.py, se encuentran las funciones para agregar, modificar, eliminar, mostrar y buscar clientes. El objetivo de este módulo es gestionar todas las operaciones relacionadas con los clientes del hotel.
* En crud_personal.py, se encuentran las funciones para agregar, modificar, eliminar, mostrar y buscar personal. El objetivo de este módulo es gestionar todas las operaciones relacionadas con el personal del hotel.
* En crud_reserva.py, se encuentran las funciones para agregar, modificar, eliminar, mostrar y buscar reservas. El objetivo de este módulo es gestionar todas las operaciones relacionadas con las reservas de habitaciones en el hotel.
* En roles.py, se encuentra la función para mostrar todos los roles. El objetivo de este módulo es visualizar todos los roles disponibles.
* En crud_habitacion.py, se encuentran las funciones para agregar, modificar, eliminar, mostrar y buscar habitaciones. El objetivo de este módulo es gestionar todas las operaciones relacionadas con las habitaciones del hotel.
* En Base_datos.py, se encuentra la conexión a la base de datos. El objetivo de este módulo es establecer la conexión con la base de datos para interactuar con ella.

## `index.py`
Este archivo actúa como el punto de entrada principal de la aplicación, proporcionando un menú que permite al usuario interactuar con las diferentes funcionalidades del sistema. Para que se puedan realizar las operaciones CRUD para clientes, personal, reservas y habitaciones mediante la llamada a las funciones definidas en los archivos mencionados anteriormente.


### VIDEO PROYECTO FINAL https://drive.google.com/drive/folders/1XzVFDskiJ3fUYuzcRpB53tqGa_5vPDaW


# Guía de Uso del Proyecto de Gestión Hotelera
Este proyecto está diseñado para gestionar diversas operaciones relacionadas con un hotel, como la administración de clientes, personal, habitaciones y reservas. A continuación, se detallan las instrucciones para instalar y utilizar la aplicación.

## Requisitos del Sistema
Para utilizar esta aplicación, se requiere:
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
- [MySQL Workbench](https://www.mysql.com/products/workbench/)
- [Python](https://www.python.org/) instalado en el sistema
- Conexión a Internet para descargar dependencias

## Instalación de Dependencias
Siga estos pasos para instalar las dependencias necesarias:

1. **Abra el símbolo del sistema (cmd)**:
   - Presione `Win + R`, escriba `cmd` y presione `Entrar`.

2. **Instale el conector MySQL**:
   - Ejecute el siguiente comando para instalar el módulo `mysql-connector-python`:
   
     pip install mysql-connector-python
     

## Configuración de la Base de Datos
- Utilice MySQL Workbench para gestionar la base de datos.
- Debe ejecutar el script Hoteles.SQL que se encuentra en el directorio aplicacion\Base_datos\

## Ejecución de la Aplicación
Siga estos pasos para ejecutar la aplicación:

1. **Abra Visual Studio Code (VS Code)**:
   - Navegue a la carpeta del proyecto en su sistema de archivos.

2. **Configure la conexión a la base de datos**:
   - Abra el archivo `Base_datos.py` y asegúrese de que las credenciales de la base de datos (usuario, contraseña, host y nombre de la base de datos) sean correctas.

3. **Ejecución del menú principal**:
   - En VS Code, abra `index.py`.
   - Ejecute el archivo `index.py` seleccionando la opción de "Ejecutar" en el menú.
     
Ejecución del menú principal:

En VS Code, abra index.py.
Ejecute el archivo index.py presionando F5 o seleccionando la opción de "Ejecutar" en el menú.

## Uso de la Aplicación
Una vez que la aplicación esté en ejecución, se presentará un menú de opciones que permite interactuar con las diferentes funcionalidades. El usuario podrá:

- Agregar, modificar, eliminar, mostrar y buscar clientes.
- Agregar, modificar, eliminar, mostrar y buscar personal.
- Agregar, modificar, eliminar, mostrar y buscar reservas.
- Visualizar roles disponibles.
- Agregar, modificar, eliminar, mostrar y buscar habitaciones.

