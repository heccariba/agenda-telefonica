 # Diario de sesiones

## Sesión 1 - 2026-10-02
### Objetivo
Preparar la estructura y la memoria del proyecto.

### Realizado
- Creadas las carpetas y plantillas iniciales.

### Comprobaciones
- `python -m src.agenda` verificado en sesión 2: muestra el menú y termina con código 0 (OK).
- `requirements.txt` contiene `pytest`, pero en sesión 2 `python -m pytest` falla porque `pytest` no está instalado (pendiente `pip install -r requirements.txt`).

### Pendiente
- Inicializar Git y crear el plan de la versión 1.

### Primer paso de la próxima sesión
Leer README, AGENTS, TODO, SESSION_LOG y CHANGELOG; después solicitar un plan sin programar.

## Sesión 2 - 2026-10-07
### Objetivo
Corregir contradicciones y huecos solo en documentos, sin programar.

### Realizado
- README: unificada restricción (sin clases, bases de datos ni decoradores salvo autorización), añadidas decisiones v1 (búsqueda exacta insensible a mayúsculas, sin duplicados, formato `Nombre - Teléfono`, fichero `data/contactos.txt` con `nombre;telefono` UTF-8, carga/guardado automático), aclarada estructura (`__init__.py`, `data/`, `docs/`) y requisitos (Python 3.10+).
- TODO: menú mínimo dado por hecho, añadido menú interactivo pendiente; concretados guardar/cargar, validación y formato; añadidas tareas de probar, revisar `.gitignore` y no subir `__pycache__/`.
- CHANGELOG: sustituido texto vago por lista concreta de lo unificado.
- SESSION_LOG: anotado resultado real de sesión 2 (menú OK, `pytest` sin instalar).

### Comprobaciones
- `python -m src.agenda` → muestra menú, código 0 (OK).
- `python -m pytest` → falla: `No module named pytest` (falta instalar).

### Pendiente
- `pip install -r requirements.txt` y repetir `pytest`.
- Inicializar Git y hacer el primer commit.

## Sesión 3 - 2026-10-07
### Objetivo
Implementar la versión 1 aprobada (solo funciones, sin clases).

### Realizado
- `src/agenda.py`: agenda como diccionario, validación, añadir, buscar por nombre/número, eliminar por nombre/número, mostrar ordenado e inverso, cargar/guardar `nombre;telefono`, menú con bucle 0-4.
- `tests/test_agenda.py`: 24 pruebas (una por comportamiento de README).
- `.gitignore`: quitada línea `data/contactos.xlsx` (no se usa Excel en v1).

### Comprobaciones
- `py_compile src/agenda.py tests/test_agenda.py` → OK.
- Lógica (añadir, duplicados, buscar, ordenar, cargar, guardar) → OK.
- E2E no interactivo (añadir Ana, mostrar, salir) → OK, fichero `Ana;600123123`.
- `python -m pytest` → pendiente: no hay `pip` ni `pytest` en este equipo.

### Pendiente
- Instalar `pip`/`pytest` y ejecutar `pytest` en verde.
- Primer commit Git.
