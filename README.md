# Chat con conversaciones largas

Un asistente de chat que responde preguntas sobre los datos de un ERP y usa tools para consultarlos. En cada turno, `build_messages()` (en `chat/context.py`) arma lo que se le manda al modelo.

`chat/api.py` y `chat/tokens.py` simulan la API del modelo y su forma de contar tokens. No los cambies: son del proveedor y no los controlamos.

`run.py` le manda a la API simulada una conversación guardada en `fixtures/`. `long_chat.json` es una charla de 8 turnos con consultas de facturas, y `short_chat.json`, una de 2.

## El problema

Con conversaciones largas, el chat se rompe:

```bash
python3 run.py fixtures/long_chat.json
```

Además, finanzas se queja de que cada respuesta cuesta cada vez más, y cobranzas ya avisó que, cuando lo arreglemos, el asistente no se puede olvidar de lo que ya consultó en la charla.

Arreglalo.

## Entrega

Cuando termines, dejá tus cambios commiteados en una rama nueva.

## Para correr

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
pytest
python3 run.py fixtures/short_chat.json
```
