# Chat con conversaciones largas

Un asistente de chat que responde preguntas sobre los datos de un ERP y usa tools para consultarlos. En cada turno, `build_messages()` (en `chat/context.py`) arma lo que se le manda al modelo.

`chat/api.py` simula la API del modelo. No lo cambies: es del proveedor y no lo controlamos.

## El problema

Con conversaciones largas, el chat se rompe:

```bash
python run.py fixtures/long_chat.json
```

Arreglalo.

## Para correr

```bash
pip install pytest
pytest
python run.py fixtures/short_chat.json
```
