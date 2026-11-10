import json
import sys
from pathlib import Path

from chat.api import send
from chat.context import build_messages
from chat.tokens import count_messages


def main(path: Path) -> None:
    history = json.loads(path.read_text(encoding="utf-8"))
    messages = build_messages(history)
    print(f"history: {len(history)} messages")
    print(f"sending: {len(messages)} messages, {count_messages(messages)} tokens")
    print(send(messages))


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "fixtures" / "short_chat.json")
