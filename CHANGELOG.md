# Historial de cambios

## [Rama con-excel - sin publicar]
### Añadido
- Dependencia `openpyxl` en `requirements.txt` para leer/escribir `.xlsx` (un Excel no es texto plano y Python no lo maneja de serie).
- Guardado en `data/contactos.xlsx` (hoja `Contactos`): fila 1 cabecera `nombre,telefono`, desde fila 2 un contacto por fila, teléfono como texto.
- Pruebas Excel: cabecera en fila 1 y teléfono guardado como texto.
### Cambiado
- `RUTA_DATOS` pasa de `data/contactos.txt` a `data/contactos.xlsx`. Sin migración ni compatibilidad con el `.txt`.
- `.gitignore` ahora ignora `data/contactos.xlsx` en vez de `data/contactos.txt`.
- Pruebas de fichero adaptadas de líneas `nombre;telefono` a filas Excel (incluye ignorar filas incompletas).

## [Sin publicar]
### Añadido
- Estructura inicial del proyecto.
- Documentación de contexto y continuidad.
- Versión 1 de la agenda: añadir, buscar por nombre/número, eliminar por nombre/número, mostrar ordenado e inverso, guardar/cargar `data/contactos.txt`, menú interactivo 0-4.
- 24 pruebas en `tests/test_agenda.py` (validación, duplicados, búsqueda, borrado, orden, fichero).
### Corregido
- Unificado programa a ejecutar: `python -m src.agenda` (menú mínimo).
- Unificada lista de lectura para agentes: `README.md`, `TODO.md`, `SESSION_LOG.md`, `AGENTS.md` y `CHANGELOG.md`.
- Unificadas tareas: menú mínimo dado por hecho, falta menú interactivo; eliminar/mostrar separados por nombre y número; pruebas para cada comportamiento.
- Coherencia carpetas-archivos: creado `src/agenda.py` mínimo, prueba inicial y renombrado a `requirements.txt`.
