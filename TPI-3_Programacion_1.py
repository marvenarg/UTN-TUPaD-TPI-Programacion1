import os

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
