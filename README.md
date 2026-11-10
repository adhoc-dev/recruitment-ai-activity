# Chat con conversaciones largas

Un asistente de chat que responde preguntas sobre los datos de un ERP y usa tools para consultarlos. En cada turno, `build_messages()` (en `chat/context.py`) arma lo que se le manda al modelo.

`chat/api.py` y `chat/tokens.py` simulan la API del modelo y su forma de contar tokens. No los cambies: son del proveedor y no los controlamos.

## El problema

Con conversaciones largas, el chat se rompe:

```bash
python3 run.py fixtures/long_chat.json
```

Además, cobranzas se queja de que en las charlas largas el asistente se olvida de lo que ya consultó, y finanzas, de que cada respuesta cuesta cada vez más.

Arreglalo.

## Para correr

```bash
python3 -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install pytest
pytest
python3 run.py fixtures/short_chat.json
```
