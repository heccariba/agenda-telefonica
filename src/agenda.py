"""Agenda telefónica - versión 1.

Gestiona contactos (nombre -> teléfono) desde la consola.
Guarda los datos en data/contactos.txt con formato nombre;telefono.
"""

RUTA_DATOS = "data/contactos.txt"
OPCION_SALIR = "0"
LONG_MIN_TELEFONO = 9
LONG_MAX_TELEFONO = 15


def mostrar_menu():
    """Muestra el menú principal en pantalla."""
    print("Agenda telefónica")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar contactos")
    print("0. Salir")


def pedir_opcion():
    """Pide la opción del menú y la devuelve sin espacios."""
    return input("Elige una opción (0 para salir): ").strip()


def pedir_nombre():
    """Pide un nombre y lo devuelve sin espacios extra."""
    return input("Nombre: ").strip()


def pedir_telefono():
    """Pide un teléfono y lo devuelve sin espacios extra."""
    return input("Teléfono: ").strip()


def nombre_es_valido(nombre):
    """Devuelve True si el nombre no está vacío."""
    return nombre.strip() != ""


def telefono_es_valido(telefono):
    """Devuelve True si tiene solo dígitos y entre 9 y 15 cifras."""
    texto = telefono.strip()
    return (
        texto.isdigit()
        and LONG_MIN_TELEFONO <= len(texto) <= LONG_MAX_TELEFONO
    )


def telefono_existe(agenda, telefono):
    """Devuelve True si ese número ya está en otro contacto."""
    return telefono in agenda.values()


def buscar_por_nombre(agenda, nombre):
    """Busca por nombre sin distinguir mayúsculas. Devuelve el teléfono o None."""
    buscado = nombre.strip().lower()
    for nombre_guardado in agenda:
        if nombre_guardado.lower() == buscado:
            return agenda[nombre_guardado]
    return None


def nombre_exact_guardado(agenda, nombre):
    """Devuelve el nombre tal como está guardado, o None si no existe."""
    buscado = nombre.strip().lower()
    for nombre_guardado in agenda:
        if nombre_guardado.lower() == buscado:
            return nombre_guardado
    return None


def buscar_por_numero(agenda, numero):
    """Busca qué contacto tiene ese número. Devuelve el nombre o None."""
    numero = numero.strip()
    for nombre_guardado, telefono in agenda.items():
        if telefono == numero:
            return nombre_guardado
    return None


def anadir_contacto(agenda, nombre, telefono):
    """Añade un contacto si es válido y no duplicado. Devuelve True o False."""
    nombre = nombre.strip()
    telefono = telefono.strip()
    if not nombre_es_valido(nombre):
        return False
    if not telefono_es_valido(telefono):
        return False
    if nombre_exact_guardado(agenda, nombre) is not None:
        return False
    if telefono_existe(agenda, telefono):
        return False
    agenda[nombre] = telefono
    return True


def eliminar_por_nombre(agenda, nombre):
    """Elimina por nombre sin distinguir mayúsculas. Devuelve True o False."""
    clave = nombre_exact_guardado(agenda, nombre)
    if clave is None:
        return False
    del agenda[clave]
    return True


def eliminar_por_numero(agenda, numero):
    """Elimina el contacto que tenga ese número. Devuelve True o False."""
    nombre = buscar_por_numero(agenda, numero)
    if nombre is None:
        return False
    del agenda[nombre]
    return True


def contactos_ordenados(agenda, inverso=False):
    """Devuelve la lista de (nombre, teléfono) ordenada por nombre."""
    return sorted(agenda.items(), key=lambda par: par[0].lower(), reverse=inverso)


def mostrar_todos(agenda, inverso=False):
    """Muestra todos los contactos ordenados. Inverso=True los muestra al revés."""
    lista = contactos_ordenados(agenda, inverso)
    if not lista:
        print("La agenda está vacía.")
        return
    for nombre, telefono in lista:
        print(nombre + " - " + telefono)


def cargar_contactos(ruta=RUTA_DATOS):
    """Carga contactos desde ruta. Si no existe, devuelve agenda vacía."""
    agenda = {}
    try:
        with open(ruta, "r", encoding="utf-8") as fichero:
            for linea in fichero:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(";")
                if len(partes) != 2:
                    continue
                anadir_contacto(agenda, partes[0].strip(), partes[1].strip())
    except FileNotFoundError:
        return {}
    return agenda


def guardar_contactos(agenda, ruta=RUTA_DATOS):
    """Guarda la agenda en ruta con formato nombre;telefono."""
    with open(ruta, "w", encoding="utf-8") as fichero:
        for nombre, telefono in agenda.items():
            fichero.write(nombre + ";" + telefono + "\n")


def opcion_anadir(agenda):
    """Pide datos y añade un contacto, guardando si tiene éxito."""
    nombre = pedir_nombre()
    telefono = pedir_telefono()
    if anadir_contacto(agenda, nombre, telefono):
        guardar_contactos(agenda)
        print("Contacto añadido.")
    else:
        print("No se pudo añadir (dato inválido o duplicado).")


def opcion_buscar(agenda):
    """Pregunta si buscar por nombre o número y muestra el resultado."""
    modo = input("¿Buscar por (1) nombre o (2) número? ").strip()
    if modo == "1":
        telefono = buscar_por_nombre(agenda, pedir_nombre())
        if telefono is None:
            print("No encontrado.")
        else:
            print("Teléfono: " + telefono)
    elif modo == "2":
        nombre = buscar_por_numero(agenda, pedir_telefono())
        if nombre is None:
            print("No encontrado.")
        else:
            print("Nombre: " + nombre)
    else:
        print("Opción de búsqueda no válida.")


def opcion_eliminar(agenda):
    """Pregunta si eliminar por nombre o número y borra, guardando si tiene éxito."""
    modo = input("¿Eliminar por (1) nombre o (2) número? ").strip()
    if modo == "1":
        if eliminar_por_nombre(agenda, pedir_nombre()):
            guardar_contactos(agenda)
            print("Contacto eliminado.")
        else:
            print("No encontrado.")
    elif modo == "2":
        if eliminar_por_numero(agenda, pedir_telefono()):
            guardar_contactos(agenda)
            print("Contacto eliminado.")
        else:
            print("No encontrado.")
    else:
        print("Opción de borrado no válida.")


def opcion_mostrar(agenda):
    """Pregunta cómo mostrar: todos, orden alfabético o inverso."""
    print("1. Todos")
    print("2. Orden alfabético")
    print("3. Orden alfabético inverso")
    modo = input("Elige cómo mostrar: ").strip()
    if modo == "1" or modo == "2":
        mostrar_todos(agenda)
    elif modo == "3":
        mostrar_todos(agenda, inverso=True)
    else:
        print("Opción no válida.")


def main():
    """Punto de entrada: carga la agenda y repite el menú hasta salir."""
    agenda = cargar_contactos()
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        if opcion == OPCION_SALIR:
            print("¡Hasta luego!")
            break
        elif opcion == "1":
            opcion_anadir(agenda)
        elif opcion == "2":
            opcion_buscar(agenda)
        elif opcion == "3":
            opcion_eliminar(agenda)
        elif opcion == "4":
            opcion_mostrar(agenda)
        else:
            print("Opción no válida, elige de 0 a 4.")


if __name__ == "__main__":
    main()
