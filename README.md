# Sistema de Gestión de Países

## Links 

### [🔗 📂 Carpeta Digital](https://drive.google.com/drive/folders/1TcXTEyjKJ9HYI_woHD6NZtlevxop7sJK?usp=drive_link)
### [🔗 ▶️ Video YouTube](https://www.youtube.com/watch?v=EUzxahH88eI)

## Descripción del programa

Este programa es una aplicación de consola desarrollada en Python que permite gestionar un catálogo de países con información sobre su población, superficie y continente al que pertenecen. El sistema utiliza un archivo CSV (`paises.csv`) como base de datos para almacenar y persistir la información de forma permanente.

### Funcionalidades principales

El programa ofrece un conjunto completo de operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y herramientas de análisis:

- **Gestión de datos**: Permite agregar nuevos países al catálogo, actualizar la población o superficie de países existentes.
- **Búsqueda y filtrado**: Ofrece búsqueda por nombre (con coincidencia parcial) y filtros avanzados por continente, rango de población o rango de superficie.
- **Ordenamiento**: Los países pueden ordenarse por nombre, población o superficie, en orden ascendente o descendente.
- **Análisis estadístico**: Calcula automáticamente estadísticas como el país con mayor y menor población, promedios de población y superficie, y distribución de países por continente.
- **Persistencia automática**: Todos los cambios realizados se guardan inmediatamente en el archivo CSV, garantizando que la información no se pierda entre sesiones.

### Arquitectura técnica

El código está completamente modularizado en funciones especializadas organizadas en las siguientes categorías:

- **Utilidades de consola**: Funciones para limpiar pantalla, pausar ejecución y dibujar menús formatados.
- **Normalización y validaciones**: Sistema robusto de validación de entrada de datos con manejo de errores.
- **Persistencia CSV**: Gestión completa de lectura y escritura del archivo CSV con validación de datos.
- **Búsquedas y filtros**: Algoritmos de búsqueda y filtrado con normalización de texto para comparaciones insensibles a mayúsculas.
- **Ordenamiento**: Implementación de algoritmo Bubble Sort para ordenar el catálogo según diferentes criterios.
- **Estadísticas**: Cálculo de métricas agregadas sobre el conjunto de datos.


---

## Instrucciones de uso

### Instalación y ejecución

1. Descargue o clone el archivo del programa (por ejemplo, `gestion_paises.py`)
2. Abra una terminal o línea de comandos
3. Navegue hasta el directorio donde guardó el archivo
4. Ejecute el programa con el comando:
   ```bash
   python gestion_paises.py
   ```

### Archivo de datos

El programa creará automáticamente un archivo `paises.csv` en el mismo directorio donde se encuentra el script si este no existe. Este archivo contiene cuatro columnas:
- `nombre`: Nombre del país
- `poblacion`: Población (número entero)
- `superficie`: Superficie en km² (número entero)
- `continente`: Continente al que pertenece

### Navegación por el menú

Al ejecutar el programa, se mostrará un menú principal con 9 opciones numeradas:

```
==============================================================
||                                                          ||
||            Menú - Gestión de Países                      ||
||                                                          ||
||                                                          ||
|| 1. Agregar país                                          ||
||                                                          ||
|| 2. Actualizar población de un país                       ||
||                                                          ||
|| 3. Actualizar superficie de un país                      ||
||                                                          ||
|| 4. Buscar país por nombre                                ||
||                                                          ||
|| 5. Filtrar países (continente / población / superficie)  ||
||                                                          ||
|| 6. Ordenar países (nombre / población / superficie)      ||
||                                                          ||
|| 7. Mostrar estadísticas                                  ||
||                                                          ||
|| 8. Mostrar todos los países                              ||
||                                                          ||
|| 9. Salir                                                 ||
||                                                          ||
==============================================================
```

Para seleccionar una opción, ingrese el número correspondiente (1-9) y presione ENTER.

### Guía de opciones del menú

**Opción 1 - Agregar país**: Permite ingresar un nuevo país con todos sus datos. El sistema validará que el nombre sea único (no se permiten duplicados), que la población y superficie sean números enteros positivos, y que ningún campo quede vacío.

**Opción 2 - Actualizar población**: Busca un país por nombre y permite modificar únicamente su población.

**Opción 3 - Actualizar superficie**: Busca un país por nombre y permite modificar únicamente su superficie.

**Opción 4 - Buscar país por nombre**: Realiza una búsqueda por coincidencia parcial. Por ejemplo, buscar "arg" encontrará "Argentina". Si hay múltiples coincidencias, mostrará una lista numerada para que seleccione el país deseado.

**Opción 5 - Filtrar países**: Presenta un submenú con tres tipos de filtros:
   - Por continente (coincidencia exacta, insensible a mayúsculas)
   - Por rango de población (mínimo y máximo)
   - Por rango de superficie (mínimo y máximo)

**Opción 6 - Ordenar países**: Presenta un submenú para elegir el campo de ordenamiento (nombre, población o superficie) y el sentido (ascendente o descendente). Muestra los resultados ordenados.

**Opción 7 - Mostrar estadísticas**: Calcula y muestra:
   - País con mayor población
   - País con menor población
   - Promedio de población
   - Promedio de superficie
   - Cantidad de países por continente

**Opción 8 - Mostrar todos los países**: Lista todos los países del catálogo con su información completa.

**Opción 9 - Salir**: Cierra el programa. Todos los datos ya están guardados automáticamente.

### Validaciones y manejo de errores

El programa incluye validaciones exhaustivas:
- No permite ingresar valores vacíos
- Solo acepta números enteros positivos para población y superficie
- Normaliza automáticamente los textos (elimina espacios extras)
- Limita la longitud de los campos (80 caracteres para nombres, 50 para continentes)
- Valida unicidad de nombres de países
- Maneja archivos CSV corruptos o mal formados ignorando filas inválidas

---

## Ejemplos de entradas y salidas

### Ejemplo 1: Agregar un nuevo país

**Entrada del usuario:**
```
Seleccione una opción (1-9): 1
Nombre del país: Argentina
Población (entero ≥ 1): 45000000
Superficie en km² (entero ≥ 1): 2780400
Continente: América del Sur
```

**Salida del programa:**
```
País agregado correctamente y guardado en el CSV.

Presione ENTER para continuar...
```

**Contenido del archivo CSV después de la operación:**
```csv
nombre,poblacion,superficie,continente
Argentina,45000000,2780400,América del Sur
```

---

### Ejemplo 2: Buscar países por nombre (coincidencia parcial)

**Entrada del usuario:**
```
Seleccione una opción (1-9): 4
Ingrese texto a buscar en el nombre: uni
```

**Salida del programa:**
```
Resultados de la búsqueda:

- Estados Unidos | Población: 331000000 | Superficie: 9833517 km² | Continente: América del Norte
- Reino Unido | Población: 67000000 | Superficie: 243610 km² | Continente: Europa

Presione ENTER para continuar...
```

---

### Ejemplo 3: Filtrar países por rango de población

**Entrada del usuario:**
```
Seleccione una opción (1-9): 5
1) Por continente
2) Por rango de población
3) Por rango de superficie
Seleccione una opción (1-3): 2

Rango de población:
Mínimo (≥ 0): 40000000
Máximo (≥ 0): 70000000
```

**Salida del programa:**
```
Listado de países:

- Argentina | Población: 45000000 | Superficie: 2780400 km² | Continente: América del Sur
- España | Población: 47000000 | Superficie: 505990 km² | Continente: Europa
- Colombia | Población: 51000000 | Superficie: 1141748 km² | Continente: América del Sur
- Reino Unido | Población: 67000000 | Superficie: 243610 km² | Continente: Europa

Presione ENTER para continuar...
```

---

### Ejemplo 4: Ordenar países por población descendente

**Entrada del usuario:**
```
Seleccione una opción (1-9): 6
1) Por nombre
2) Por población
3) Por superficie
Seleccione una opción (1-3): 2

Orden:
1) Ascendente
2) Descendente
Seleccione una opción (1-2): 2
```

**Salida del programa:**
```
Países ordenados:

Listado de países:

- China | Población: 1400000000 | Superficie: 9596961 km² | Continente: Asia
- India | Población: 1380000000 | Superficie: 3287263 km² | Continente: Asia
- Estados Unidos | Población: 331000000 | Superficie: 9833517 km² | Continente: América del Norte
- Indonesia | Población: 273000000 | Superficie: 1904569 km² | Continente: Asia
- Brasil | Población: 212000000 | Superficie: 8515767 km² | Continente: América del Sur
[...]

Presione ENTER para continuar...
```

---

### Ejemplo 5: Mostrar estadísticas

**Entrada del usuario:**
```
Seleccione una opción (1-9): 7
```

**Salida del programa:**
```
--- Estadísticas ---
País con mayor población: China (1400000000)
País con menor población: Islandia (366000)
Promedio de población: 156733333.33
Promedio de superficie: 2847291.50

Cantidad de países por continente:
 - Asia: 4
 - América del Norte: 2
 - América del Sur: 3
 - Europa: 5
 - África: 2
 - Oceanía: 1

Presione ENTER para continuar...
```

---

### Ejemplo 6: Actualizar población con búsqueda y selección

**Entrada del usuario:**
```
Seleccione una opción (1-9): 2
Ingrese el nombre (o parte del nombre) del país: españa
```

**Salida del programa:**
```
Se encontraron varios países:
1. España | Población: 47000000 | Superficie: 505990 km² | Continente: Europa

Seleccione el número del país: 1

País seleccionado: España
Nueva población (≥ 1): 47500000
Población actualizada y guardada en el CSV.

Presione ENTER para continuar...
```

---

### Ejemplo 7: Intento de agregar país duplicado

**Entrada del usuario:**
```
Seleccione una opción (1-9): 1
Nombre del país: Argentina
```

**Salida del programa:**
```
Ya existe un país con ese nombre. No se puede duplicar.

Presione ENTER para continuar...
```

---

### Ejemplo 8: Validación de entrada inválida

**Entrada del usuario:**
```
Seleccione una opción (1-9): 1
Nombre del país: Brasil
Población (entero ≥ 1): -500
```

**Salida del programa:**
```
Entrada inválida. Debe ser un entero mayor a 0.
Población (entero ≥ 1): abc
Entrada inválida. Debe ser un entero mayor a 0.
Población (entero ≥ 1): 212000000
Superficie en km² (entero ≥ 1): 8515767
Continente: América del Sur

País agregado correctamente y guardado en el CSV.
```

# Participación de los Integrantes

## Metodología de trabajo

El desarrollo del proyecto se realizó mediante una colaboración continua entre ambos integrantes del grupo, utilizando Git y GitHub como herramientas principales para el control de versiones y la integración del código. Se estableció un flujo de trabajo basado en ramas (branches) y pull requests (PR) para garantizar la revisión y calidad del código antes de su integración a la rama principal.

## Distribución de responsabilidades

### Integrante 1: Desarrollo de funcionalidades principales y lógica de negocio

**Funciones desarrolladas:**
- `cargar_paises()`: Implementación de la lectura del archivo CSV con validación robusta de datos
- `guardar_paises()`: Sistema de persistencia con manejo de escritura en CSV
- `agregar_pais()`: Lógica completa para agregar países con validación de unicidad
- `actualizar_poblacion_pais()`: Funcionalidad de actualización de población
- `actualizar_superficie_pais()`: Funcionalidad de actualización de superficie
- `buscar_indices_por_nombre()`: Algoritmo de búsqueda con normalización de texto
- `seleccionar_pais_por_nombre()`: Sistema de selección interactivo con múltiples coincidencias


### Integrante 2: Interfaz de usuario, utilidades y algoritmos de procesamiento

**Funciones desarrolladas:**
- `limpiar()`: Función multiplataforma para limpiar consola
- `pausar()`: Sistema de pausa de ejecución
- `dibujar_menu()`: Diseño e implementación del formato visual del menú
- `leer_opcion_menu()`: Validación de entrada numérica para navegación
- `leer_entero_positivo()`: Validador genérico de enteros con configuración flexible
- `leer_texto_no_vacio()`: Validador de texto con límite de caracteres
- `normalizar_texto()`: Utilidad de limpieza de espacios
- `normalizar_clave_nombre()`: Normalización específica para claves de búsqueda
- `inicializar_csv()`: Creación automática del archivo con encabezados
- `filtrar_por_continente()`: Implementación de filtro por continente
- `filtrar_por_rango()`: Filtro genérico por rangos numéricos
- `ordenar_paises()`: Implementación del algoritmo Bubble Sort
- `mostrar_estadisticas()`: Cálculo de métricas y estadísticas agregadas
- `mostrar_paises()`: Función de visualización formateada
- `main()`: Estructura del menú principal y flujo del programa


### Funciones desarrolladas en conjunto

Las siguientes funcionalidades fueron diseñadas en conjunto:

- `buscar_pais_por_nombre()`: Integración de búsqueda con visualización
- `filtrar_paises()`: Menú de filtrado que combina múltiples criterios
- `ordenar_paises_menu()`: Interfaz completa de ordenamiento

## Proceso de integración

El flujo de trabajo establecido fue el siguiente:

1. **Desarrollo en ramas**: Cada integrante trabajó en su rama específica según la funcionalidad asignada
2. **Revisión de código**: Al completar una funcionalidad, se creaba un pull request hacia la rama principal
3. **Code review**: El otro integrante revisaba el código, sugería mejoras y solicitaba cambios cuando era necesario
4. **Refactoring**: Se realizaban ajustes de estilo, optimizaciones y mejoras de legibilidad
5. **Merge**: Una vez aprobado, el código se integraba a la rama principal
6. **Testing conjunto**: Ambos integrantes probaban la funcionalidad integrada para detectar posibles errores de integración

## Herramientas utilizadas

- **Control de versiones**: Git y GitHub
- **Comunicación**: Reuniones virtuales para revisión de arquitectura
- **Editor de código**: Cada integrante utilizó su entorno preferido
- **Testing**: Pruebas manuales realizadas por ambos integrantes con diferentes casos de uso
