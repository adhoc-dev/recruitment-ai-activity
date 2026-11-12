import json
from pathlib import Path

from chat.api import send
from chat.context import build_messages

FIXTURES = Path(__file__).parent.parent / "fixtures"


def load(name: str) -> list[dict]:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def test_short_chat():
    assert send(build_messages(load("short_chat.json"))) == "ok"
