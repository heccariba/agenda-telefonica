 # Plan y tareas

## En curso
- [ ] Validar versión 1 con `pytest` instalado (falta `pip` en este equipo).

## Pendientes
- [ ] Inicializar Git (hacer el primer commit).
- [ ] Actualizar documentación.

## Terminadas
- [x] Acordar el plan de la versión 1.
- [x] Crear estructura inicial.
- [x] Crear menú mínimo `src/agenda.py` que se imprime y se ejecuta (`mostrar_menu()` + `OPCION_SALIR`).
- [x] Definir formato de fichero: `data/contactos.txt` con `nombre;telefono` por línea en UTF-8.
- [x] Corregir `requeriments.txt` a `requirements.txt`.
- [x] Completar menú interactivo con bucle y opciones 0-4.
- [x] Añadir contactos.
- [x] Buscar contactos por nombre y por número.
- [x] Eliminar contactos por nombre y por número.
- [x] Mostrar todos los contactos, en orden alfabético e inverso.
- [x] Guardar y cargar datos en `data/contactos.txt` (`nombre;telefono` UTF-8).
- [x] Crear pruebas para cada comportamiento (`tests/test_agenda.py`, 24 pruebas).
- [x] Validar: nombre no vacío, teléfono solo dígitos de 9 a 15 cifras.
- [x] Probar menú y lógica con verificación no interactiva (E2E OK).
- [x] Revisar `.gitignore` y no subir `__pycache__/` ni `data/contactos.txt` (quitada línea `xlsx`).
