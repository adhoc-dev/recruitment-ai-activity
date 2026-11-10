import json
import sys

from chat.api import send
from chat.context import build_messages
from chat.tokens import count_messages


def main(path: str) -> None:
    with open(path, encoding="utf-8") as f:
        history = json.load(f)
    messages = build_messages(history)
    print(f"history: {len(history)} messages")
    print(f"sending: {len(messages)} messages, {count_messages(messages)} tokens")
    print(send(messages))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "fixtures/short_chat.json")
