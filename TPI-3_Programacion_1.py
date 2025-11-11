# Se importan las librerías necesarias
import os
import csv

# ------------------------- Utilidades de consola -------------------------

def limpiar():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecución hasta que el usuario presione ENTER."""
    input("\nPresione ENTER para continuar...")

def dibujar_menu(titulo: str, opciones: list, ancho: int = 56):
    """Dibuja el menú de opciones en la consola."""
    barra = "=" * ancho
    print(barra)

    # Espacio arriba del título
    print(f"||{' ' * (ancho - 4)}||")
    linea_titulo = f"|| {titulo.center(ancho - 6)} ||"
    print(linea_titulo)
    print(f"||{' ' * (ancho - 4)}||")

    # Línea en blanco extra
    print(f"||{' ' * (ancho - 4)}||")

    # Opciones
    i = 0
    while i < len(opciones):
        texto = f"{i+1}. {opciones[i]}"
        print(f"|| {texto.ljust(ancho - 6)} ||")
        print(f"||{' ' * (ancho - 4)}||")
        i += 1

    # Línea en blanco final y barra inferior
    print(f"||{' ' * (ancho - 4)}||")
    print(barra)

def leer_opcion_menu(min_op: int, max_op: int) -> int:
    """Lee una opción numérica del menú. Devuelve 0 si es inválida."""
    s = input(f"Seleccione una opción ({min_op}-{max_op}): ").strip()
    if s.isdigit():
        n = int(s)
        if min_op <= n <= max_op:
            return n
    return 0

# ------------------------- Normalización / Validaciones -------------------------

def normalizar_texto(s: str) -> str:
    """Quita espacios extras y colapsa espacios internos."""
    s = s.strip()
    s = " ".join(s.split())
    return s

def normalizar_clave_nombre(s: str) -> str:
    """Normaliza un nombre para comparaciones insensibles a mayúsculas y espacios."""
    return normalizar_texto(s).lower()

def leer_entero_positivo(msg: str, permitir_cero: bool) -> int:
    """Lee un entero >= 1 (o >=0 si permitir_cero=True)."""
    while True:
        s = input(msg).strip()
        if s.isdigit():
            n = int(s)
            if n > 0 or (permitir_cero and n == 0):
                return n
        print("Entrada inválida. Debe ser un entero mayor a 0" +
              ("" if not permitir_cero else " o igual a 0") + ".")

def leer_texto_no_vacio(msg: str, maxchar: int) -> str:
    """Lee un texto no vacío y con límite de caracteres."""
    while True:
        s = input(msg).strip()
        if s == "":
            print("No se permite un valor vacío. Intente nuevamente.")
        elif len(s) > maxchar:
            print(f"El texto supera el máximo permitido ({maxchar} caracteres).")
        else:
            return s

# ------------------------- Persistencia CSV -------------------------

def inicializar_csv(ruta_csv: str) -> None:
    """Crea el archivo CSV vacío con encabezados si no existe."""
    if not os.path.exists(ruta_csv):
        with open(ruta_csv, "w", encoding="utf-8", newline="") as f:
            escritor = csv.writer(f)
            escritor.writerow(["nombre", "poblacion", "superficie", "continente"])

def cargar_paises(ruta_csv: str) -> list:
    """Carga el CSV de países a una lista de diccionarios."""
    paises = []
    if not os.path.exists(ruta_csv):
        return paises  # archivo no existe: lista vacía

    with open(ruta_csv, "r", encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f)
        if lector.fieldnames is None:
            return paises

        for fila in lector:
            if ("nombre" not in fila or
                "poblacion" not in fila or
                "superficie" not in fila or
                "continente" not in fila):
                continue  # fila mal formada

            nombre = normalizar_texto(fila["nombre"])
            pobl_str = fila["poblacion"].strip()
            sup_str = fila["superficie"].strip()
            cont = normalizar_texto(fila["continente"])

            if nombre == "" or cont == "":
                continue

            if not pobl_str.isdigit() or not sup_str.isdigit():
                continue

            pobl = int(pobl_str)
            sup = int(sup_str)
            if pobl < 0 or sup < 0:
                continue

            paises.append({
                "nombre": nombre,
                "poblacion": pobl,
                "superficie": sup,
                "continente": cont
            })
    return paises

def guardar_paises(ruta_csv: str, paises: list) -> None:
    """Guarda la lista de países en el CSV (lo crea si no existe y lo sobrescribe)."""
    with open(ruta_csv, "w", encoding="utf-8", newline="") as f:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)

# ------------------------- Búsquedas, filtros y ordenamientos -------------------------

def buscar_indices_por_nombre(paises: list, texto_busqueda: str) -> list:
    """Devuelve una lista de índices cuyos nombres contienen el texto buscado (normalizado)."""
    objetivo = normalizar_clave_nombre(texto_busqueda)
    indices = []
    for index, pais in enumerate(paises):
        nombre_norm = normalizar_clave_nombre(pais["nombre"])
        if objetivo in nombre_norm:
            indices.append(index)
    return indices

def seleccionar_pais_por_nombre(paises: list) -> int:
    """
    Permite buscar un país por nombre (parcial) y seleccionar uno si hay múltiples coincidencias.
    Devuelve el índice del país en la lista o -1 si no hay selección posible.
    """
    if len(paises) == 0:
        print("No hay países cargados.")
        return -1

    texto = leer_texto_no_vacio("Ingrese el nombre (o parte del nombre) del país: ", 80)
    indices = buscar_indices_por_nombre(paises, texto)

    if len(indices) == 0:
        print("No se encontraron países que coincidan con la búsqueda.")
        return -1

    if len(indices) == 1:
        return indices[0]

    print("\nSe encontraron varios países:")
    i = 0
    while i < len(indices):
        p = paises[indices[i]]
        print(f"{i+1}. {p['nombre']} | Población: {p['poblacion']} | "
              f"Superficie: {p['superficie']} km² | Continente: {p['continente']}")
        i += 1
    sel = leer_entero_positivo("Seleccione el número del país: ", permitir_cero=False)
    if sel < 1 or sel > len(indices):
        print("Selección inválida.")
        return -1
    return indices[sel - 1]

def filtrar_por_continente(paises: list, continente: str) -> list:
    """Filtra países por continente (comparación normalizada)."""
    cont_norm = normalizar_clave_nombre(continente)
    resultado = []
    i = 0
    while i < len(paises):
        if normalizar_clave_nombre(paises[i]["continente"]) == cont_norm:
            resultado.append(paises[i])
        i += 1
    return resultado

def filtrar_por_rango(paises: list, campo: str, minimo: int, maximo: int) -> list:
    """Filtra países por un rango numérico (poblacion o superficie)."""
    resultado = []
    i = 0
    while i < len(paises):
        valor = paises[i][campo]
        if minimo <= valor <= maximo:
            resultado.append(paises[i])
        i += 1
    return resultado

def ordenar_paises(paises: list, campo: str, ascendente: bool) -> None:   
    """Ordena la lista de países usando bubble sort según el campo indicado.
    Modifica directamente la misma lista (sin crear otra), en orden ascendente
    si ascendente es True, o descendente si es False."""
    n = len(paises)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            a = paises[j][campo]
            b = paises[j+1][campo]
            cambiar = (a > b) if ascendente else (a < b)
            if cambiar:
                tmp = paises[j]
                paises[j] = paises[j+1]
                paises[j+1] = tmp
            j += 1
        i += 1

# ------------------------- Estadísticas -------------------------

def mostrar_estadisticas(paises: list) -> None:
    """Muestra estadísticas generales del catálogo de países."""
    if len(paises) == 0:
        print("\nNo hay países cargados, no se pueden calcular estadísticas.")
        return

    max_pais = paises[0]
    min_pais = paises[0]
    suma_pobl = 0
    suma_sup = 0

    i = 0
    while i < len(paises):
        p = paises[i]
        suma_pobl += p["poblacion"]
        suma_sup += p["superficie"]

        if p["poblacion"] > max_pais["poblacion"]:
            max_pais = p
        if p["poblacion"] < min_pais["poblacion"]:
            min_pais = p

        i += 1

    prom_pobl = suma_pobl / len(paises)
    prom_sup = suma_sup / len(paises)

    conteo_cont = {}
    i = 0
    while i < len(paises):
        cont = paises[i]["continente"]
        if cont in conteo_cont:
            conteo_cont[cont] += 1
        else:
            conteo_cont[cont] = 1
        i += 1

    print("\n--- Estadísticas ---")
    print(f"País con mayor población: {max_pais['nombre']} ({max_pais['poblacion']})")
    print(f"País con menor población: {min_pais['nombre']} ({min_pais['poblacion']})")
    print(f"Promedio de población: {prom_pobl:.2f}")
    print(f"Promedio de superficie: {prom_sup:.2f}")
    print("\nCantidad de países por continente:")
    for cont, cant in conteo_cont.items():
        print(f" - {cont}: {cant}")

# ------------------------- Operaciones sobre países -------------------------

def mostrar_paises(paises: list) -> None:
    """Muestra todos los países almacenados."""
    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return
    print("\nListado de países:\n")
    i = 0
    while i < len(paises):
        p = paises[i]
        print(f"- {p['nombre']} | Población: {p['poblacion']} | "
              f"Superficie: {p['superficie']} km² | Continente: {p['continente']}")
        i += 1

def agregar_pais(paises: list, ruta_csv: str) -> None:
    """Agrega un país nuevo, verificando que el nombre sea único y que los campos no estén vacíos."""
    print("\n1) Agregar país")
    nombre = normalizar_texto(leer_texto_no_vacio("Nombre del país: ", 80))

    # Validar que no exista ya (unicidad por nombre normalizado)
    if len(buscar_indices_por_nombre(paises, nombre)) > 0:
        print("Ya existe un país con ese nombre. No se puede duplicar.")
        return

    poblacion = leer_entero_positivo("Población (entero ≥ 1): ", permitir_cero=False)
    superficie = leer_entero_positivo("Superficie en km² (entero ≥ 1): ", permitir_cero=False)
    continente = normalizar_texto(leer_texto_no_vacio("Continente: ", 50))

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })

    guardar_paises(ruta_csv, paises)
    print("\nPaís agregado correctamente y guardado en el CSV.")

def actualizar_poblacion_pais(paises: list, ruta_csv: str) -> None:
    """Actualiza solo la población de un país."""
    print("\n2) Actualizar población de un país")
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    idx = seleccionar_pais_por_nombre(paises)
    if idx == -1:
        return

    print(f"\nPaís seleccionado: {paises[idx]['nombre']}")
    nueva_pobl = leer_entero_positivo("Nueva población (≥ 1): ", permitir_cero=False)

    paises[idx]["poblacion"] = nueva_pobl
    guardar_paises(ruta_csv, paises)
    print("Población actualizada y guardada en el CSV.")

def actualizar_superficie_pais(paises: list, ruta_csv: str) -> None:
    """Actualiza solo la superficie de un país."""
    print("\n3) Actualizar superficie de un país")
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    idx = seleccionar_pais_por_nombre(paises)
    if idx == -1:
        return

    print(f"\nPaís seleccionado: {paises[idx]['nombre']}")
    nueva_sup = leer_entero_positivo("Nueva superficie (≥ 1): ", permitir_cero=False)

    paises[idx]["superficie"] = nueva_sup
    guardar_paises(ruta_csv, paises)
    print("Superficie actualizada y guardada en el CSV.")

def buscar_pais_por_nombre(paises: list) -> None:
    """Busca países por nombre (coincidencia parcial) y los muestra."""
    print("\n4) Buscar país por nombre")
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    texto = leer_texto_no_vacio("Ingrese texto a buscar en el nombre: ", 80)
    indices = buscar_indices_por_nombre(paises, texto)

    if len(indices) == 0:
        print("No se encontraron países que coincidan con la búsqueda.")
        return

    print("\nResultados de la búsqueda:\n")
    i = 0
    while i < len(indices):
        p = paises[indices[i]]
        print(f"- {p['nombre']} | Población: {p['poblacion']} | "
              f"Superficie: {p['superficie']} km² | Continente: {p['continente']}")
        i += 1

def filtrar_paises(paises: list) -> None:
    """Submenú para filtrar países."""
    print("\n5) Filtrar países")
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    print("1) Por continente")
    print("2) Por rango de población")
    print("3) Por rango de superficie")
    op = leer_opcion_menu(1, 3)

    if op == 1:
        cont = leer_texto_no_vacio("Ingrese continente: ", 50)
        resultado = filtrar_por_continente(paises, cont)
    elif op == 2:
        print("\nRango de población:")
        min_p = leer_entero_positivo("Mínimo (≥ 0): ", permitir_cero=True)
        max_p = leer_entero_positivo("Máximo (≥ 0): ", permitir_cero=True)
        if max_p < min_p:
            aux = min_p
            min_p = max_p
            max_p = aux
        resultado = filtrar_por_rango(paises, "poblacion", min_p, max_p)
    elif op == 3:
        print("\nRango de superficie:")
        min_s = leer_entero_positivo("Mínimo (≥ 0): ", permitir_cero=True)
        max_s = leer_entero_positivo("Máximo (≥ 0): ", permitir_cero=True)
        if max_s < min_s:
            aux = min_s
            min_s = max_s
            max_s = aux
        resultado = filtrar_por_rango(paises, "superficie", min_s, max_s)
    else:
        print("Opción inválida.")
        return

    if len(resultado) == 0:
        print("\nNo se encontraron países con ese criterio.")
    else:
        mostrar_paises(resultado)

def ordenar_paises_menu(paises: list) -> None:
    """Submenú para ordenar países."""
    print("\n6) Ordenar países")
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    print("1) Por nombre")
    print("2) Por población")
    print("3) Por superficie")
    op = leer_opcion_menu(1, 3)

    print("\nOrden:")
    print("1) Ascendente")
    print("2) Descendente")
    ord_op = leer_opcion_menu(1, 2)
    asc = (ord_op == 1)

    if op == 1:
        ordenar_paises(paises, "nombre", ascendente=asc)
    elif op == 2:
        ordenar_paises(paises, "poblacion", ascendente=asc)
    elif op == 3:
        ordenar_paises(paises, "superficie", ascendente=asc)
    else:
        print("Opción inválida.")
        return

    print("\nPaíses ordenados:")
    mostrar_paises(paises)

# ------------------------- Menú principal TPI Países -------------------------

def main():
    # Ruta del CSV en la misma carpeta que esté el .py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(base_dir, "paises.csv")

    # Crea el CSV vacío con encabezados si no existe
    inicializar_csv(ruta_csv)

    # Se carga el catálogo inicial desde el CSV
    paises = cargar_paises(ruta_csv)

    ancho_menu = 62
    opciones = [
        "Agregar país",
        "Actualizar población de un país",
        "Actualizar superficie de un país",
        "Buscar país por nombre",
        "Filtrar países (continente / población / superficie)",
        "Ordenar países (nombre / población / superficie)",
        "Mostrar estadísticas",
        "Mostrar todos los países",
        "Salir"
    ]

    seguir = True
    while seguir:
        limpiar()
        dibujar_menu("Menú - Gestión de Países", opciones, ancho_menu)
        opcion = leer_opcion_menu(1, 9)

        limpiar()
        match opcion:
            case 1:
                agregar_pais(paises, ruta_csv)
                pausar()
            case 2:
                actualizar_poblacion_pais(paises, ruta_csv)
                pausar()
            case 3:
                actualizar_superficie_pais(paises, ruta_csv)
                pausar()
            case 4:
                buscar_pais_por_nombre(paises)
                pausar()
            case 5:
                filtrar_paises(paises)
                pausar()
            case 6:
                ordenar_paises_menu(paises)
                pausar()
            case 7:
                mostrar_estadisticas(paises)
                pausar()
            case 8:
                print("\n8) Mostrar todos los países")
                mostrar_paises(paises)
                pausar()
            case 9:
                print("Saliendo del programa...")
                seguir = False
            case _:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 9.")
                pausar()

# Llamada directa a la función principal main() para iniciar el programa.
main()
