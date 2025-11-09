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
def buscar_indices_por_nombre(paises: list, texto_busqueda: str) -> list:
    """Devuelve una lista de índices cuyos nombres contienen el texto buscado (normalizado)."""
    objetivo = normalizar_clave_nombre(texto_busqueda)
    indices = []
    for index, pais in enumerate(paises):
        nombre_norm = normalizar_clave_nombre(pais["nombre"])
        if objetivo in nombre_norm:
            indices.append(index)
    return indices

# ------------------------- Menú principal TPI Países -------------------------

def main():
    # Más adelante acá se valida si existe el archivo CSV de países, y en el caso que no exista se crea uno en blanco sólo con los campos, por ahora es solo el menú.
    ancho_menu = 62
    opciones = [
        "Agregar país",
        "Actualizar población",
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
                print("1) Agregar país")
                # TODO: llamar a la función que agrega un país nuevo
                pausar()
            case 2:
                print("2) Actualizar la población de un país")
                # TODO: llamar a la función que actualiza la población de un país
                pausar()
            case 3:
                print("3) Actualizar la superficie de un país")
                # TODO: llamar a la función que actualiza la superficie de un país
                pausar()                    
            case 4:
                print("4) Buscar país por nombre")
                # TODO: llamar a la función de búsqueda por nombre
                pausar()
            case 5:
                print("5) Filtrar países")
                # TODO: llamar a la función de filtros (continente / rango población / rango superficie)
                pausar()
            case 6:
                print("6) Ordenar países")
                # TODO: llamar a la función de ordenamiento
                pausar()
            case 7:
                print("7) Mostrar estadísticas")
                # TODO: llamar a la función que calcula y muestra estadísticas
                pausar()
            case 8:
                print("8) Mostrar todos los países")
                # TODO: llamar a la función que lista todos los países
                pausar()
            case 9:
                print("Saliendo del programa...")
                seguir = False
            case _:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 8.")
                pausar()

# Llamada directa a la función principal main () para iniciar el programa.
main()
