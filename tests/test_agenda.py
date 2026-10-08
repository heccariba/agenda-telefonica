"""Pruebas de la agenda telefónica - versión 1.

Cada prueba comprueba un comportamiento de README Decisiones v1.
"""

from src import agenda


def test_mostrar_menu_existe():
    assert callable(agenda.mostrar_menu)


def test_opcion_salir_es_cero():
    assert agenda.OPCION_SALIR == "0"


def test_nombre_no_vacio_es_valido():
    assert agenda.nombre_es_valido("Ana") is True


def test_nombre_vacio_no_es_valido():
    assert agenda.nombre_es_valido("   ") is False


def test_telefono_9_cifras_es_valido():
    assert agenda.telefono_es_valido("600123123") is True


def test_telefono_con_letras_no_es_valido():
    assert agenda.telefono_es_valido("600abc123") is False


def test_telefono_corto_no_es_valido():
    assert agenda.telefono_es_valido("123") is False


def test_telefono_largo_no_es_valido():
    assert agenda.telefono_es_valido("1" * 16) is False


def test_anadir_contacto_valido():
    mi_agenda = {}
    assert agenda.anadir_contacto(mi_agenda, "Ana", "600123123") is True
    assert mi_agenda == {"Ana": "600123123"}


def test_anadir_nombre_duplicado_falla():
    mi_agenda = {"Ana": "600123123"}
    assert agenda.anadir_contacto(mi_agenda, "ana", "600999999") is False
    assert mi_agenda == {"Ana": "600123123"}


def test_anadir_numero_duplicado_falla():
    mi_agenda = {"Ana": "600123123"}
    assert agenda.anadir_contacto(mi_agenda, "Luis", "600123123") is False
    assert "Luis" not in mi_agenda


def test_buscar_por_nombre_ignora_mayusculas():
    mi_agenda = {"Ana": "600123123"}
    assert agenda.buscar_por_nombre(mi_agenda, "ANA") == "600123123"


def test_buscar_por_nombre_inexistente_da_none():
    assert agenda.buscar_por_nombre({}, "Ana") is None


def test_buscar_por_numero_encuentra_nombre():
    mi_agenda = {"Ana": "600123123"}
    assert agenda.buscar_por_numero(mi_agenda, "600123123") == "Ana"


def test_buscar_por_numero_inexistente_da_none():
    assert agenda.buscar_por_numero({}, "600123123") is None


def test_eliminar_por_nombre_borra():
    mi_agenda = {"Ana": "600123123"}
    assert agenda.eliminar_por_nombre(mi_agenda, "ana") is True
    assert mi_agenda == {}


def test_eliminar_por_nombre_inexistente_falla():
    mi_agenda = {"Ana": "600123123"}
    assert agenda.eliminar_por_nombre(mi_agenda, "Luis") is False
    assert mi_agenda == {"Ana": "600123123"}


def test_eliminar_por_numero_borra():
    mi_agenda = {"Ana": "600123123"}
    assert agenda.eliminar_por_numero(mi_agenda, "600123123") is True
    assert mi_agenda == {}


def test_eliminar_por_numero_inexistente_falla():
    mi_agenda = {"Ana": "600123123"}
    assert agenda.eliminar_por_numero(mi_agenda, "600000000") is False
    assert mi_agenda == {"Ana": "600123123"}


def test_contactos_ordenados_alfabetico():
    mi_agenda = {"Luis": "600111111", "Ana": "600123123"}
    nombres = [nombre for nombre, _ in agenda.contactos_ordenados(mi_agenda)]
    assert nombres == ["Ana", "Luis"]


def test_contactos_ordenados_inverso():
    mi_agenda = {"Luis": "600111111", "Ana": "600123123"}
    nombres = [n for n, _ in agenda.contactos_ordenados(mi_agenda, inverso=True)]
    assert nombres == ["Luis", "Ana"]


def test_guardar_y_cargar(tmp_path):
    mi_agenda = {"Ana": "600123123", "Luis": "600111111"}
    ruta = str(tmp_path / "contactos.txt")
    agenda.guardar_contactos(mi_agenda, ruta)
    assert agenda.cargar_contactos(ruta) == mi_agenda


def test_cargar_fichero_inexistente_da_vacia(tmp_path):
    ruta = str(tmp_path / "no_existe.txt")
    assert agenda.cargar_contactos(ruta) == {}


def test_cargar_ignora_lineas_malas(tmp_path):
    ruta = str(tmp_path / "contactos.txt")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("Ana;600123123\nsin_separador\nLuis;600111111\n")
    assert agenda.cargar_contactos(ruta) == {"Ana": "600123123", "Luis": "600111111"}


