# PFU-111 - Semana 13
## Registro de solicitudes de soporte técnico

### Descripción del proyecto

Este proyecto consiste en una aplicación de escritorio desarrollada en Python para registrar y consultar solicitudes de soporte técnico. Permite almacenar los datos del estudiante, el tipo de problema, su descripción y el nivel de prioridad.

La información se guarda en un archivo CSV, lo que permite conservar las solicitudes registradas y consultarlas posteriormente.

### Funcionalidades principales

- **Registrar solicitudes:** permite ingresar los datos del solicitante y describir el problema.
- **Consultar solicitudes:** muestra las solicitudes almacenadas en el archivo CSV.
- **Validar datos:** verifica que los campos obligatorios estén completos y que las opciones seleccionadas sean válidas.
- **Seleccionar tipo de solicitud:** permite elegir entre equipo, software y conectividad.
- **Asignar prioridad:** permite establecer la prioridad como baja, media o alta.
- **Limpiar formulario:** borra los datos ingresados para registrar una nueva solicitud.
- **Guardar información:** almacena los registros en el archivo `solicitudes.csv`.

### Tecnologías utilizadas

- **Python:** lenguaje de programación utilizado para desarrollar la aplicación.
- **Tkinter:** biblioteca para crear la interfaz gráfica.
- **ttk:** componentes gráficos para formularios, botones y listas desplegables.
- **CSV:** formato utilizado para almacenar y consultar las solicitudes.
- **OS:** módulo utilizado para gestionar la ruta del archivo y verificar su existencia.

### Datos registrados

Cada solicitud contiene los siguientes campos:

| Campo | Descripción |
|---|---|
| Nombre | Nombre del solicitante. |
| Código | Código de estudiante. |
| Tipo | Equipo, software o conectividad. |
| Descripción | Detalle del problema técnico. |
| Prioridad | Bajo, medio o alto. |

### Validaciones implementadas

El programa verifica que:

1. El nombre del solicitante no esté vacío.
2. El código de estudiante no esté vacío.
3. Se seleccione un tipo de solicitud válido.
4. La descripción del problema no esté vacía.
5. Se seleccione una prioridad válida.

Si existen errores, el programa muestra los campos que deben corregirse antes de guardar la solicitud.

### Requisitos

- Tener Python 3 instalado.
- Disponer de las bibliotecas `tkinter`, `csv` y `os`, incluidas normalmente en Python.
- Contar con un sistema operativo compatible con Tkinter.

### Instalación y ejecución

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto.
3. Ejecutar el archivo Python desde una terminal:

   ```bash
   python "solicitudes_soporte (1).py"
   ```

4. Completar los campos del formulario.
5. Presionar **Registrar solicitud** para guardar la información.
6. Utilizar **Consultar solicitudes** para visualizar los registros almacenados.

### Almacenamiento de información

Los registros se guardan en un archivo llamado `solicitudes.csv`, ubicado en la misma carpeta que el programa.

El archivo se crea automáticamente al registrar la primera solicitud y contiene los encabezados de las columnas junto con los datos ingresados.

### Objetivo del proyecto

Desarrollar una aplicación sencilla que facilite el registro y la consulta de solicitudes de soporte técnico, aplicando conceptos de programación en Python, funciones, validación de datos, manejo de archivos CSV e interfaces gráficas.
**Actividad:** Semana 13 - Registro de solicitudes de soporte técnico
