# Agenda Telefónica

## Objetivo
Crear una aplicación de consola en Python para gestionar contactos.

## Funcionalidades de la versión 1
- Añadir contactos.
- Buscar contactos por nombre.
- Buscar contactos por número.
- Eliminar contactos por nombre.
- Eliminar contactos por número.
- Mostrar todos los contactos.
- Mostrar todos los contactos en orden alfabético.
- Mostrar todos los contactos en orden alfabético inverso.
- Guardar y cargar contactos desde un fichero de texto.

## Restricciones didácticas
- Programación estructurada.
- Funciones pequeñas y nombres descriptivos.
- Sin clases, bases de datos ni decoradores en la versión 1 salvo autorización.
- Código comprensible para alumnado de 2.º de Bachillerato.

## Decisiones de la versión 1 (para poder programar y probar)
- Búsqueda por nombre: exacta e insensible a mayúsculas (da igual `Ana` que `ana`).
- No se permiten dos contactos con el mismo nombre.
- Un mismo número no se repite en dos contactos distintos.
- El teléfono solo acepta dígitos y debe tener entre 9 y 15 cifras. El nombre no puede estar vacío.
- Mostrar un contacto con el formato `Nombre - Teléfono` (ejemplo: `Ana - 600123123`).
- Fichero de datos: `data/contactos.txt`, con una línea por contacto `nombre;telefono` en UTF-8.
- Si el fichero no existe al iniciar, se empieza con la agenda vacía (no es un error).
- La agenda se carga sola al iniciar y se guarda sola al añadir o eliminar.

## Estructura
- `src/agenda.py`: programa principal (de momento, solo menú mínimo que se imprime).
- `src/`: código del programa (`__init__.py` vacío solo para importar en pruebas).
- `tests/`: pruebas automáticas con `pytest` (ver `requirements.txt`).
- `data/`: datos de ejecución (`contactos.txt` con formato `nombre;telefono`, ignorado por Git).
- `docs/`: documentación adicional (vacío en versión 1, reservado para explicaciones extra).

## Ejecución
```bash
python -m src.agenda
```

## Pruebas
Requisitos: Python 3.10 o superior y `pytest` (ver `requirements.txt`).
```bash
pip install -r requirements.txt
python -m src.agenda
python -m pytest
```