import json
import math


def count_tokens(message: dict) -> int:
    """Rough estimate: about 4 characters per token, plus a fixed cost per message."""
    text = message.get("content") or ""
    if message.get("tool_calls"):
        text += json.dumps(message["tool_calls"], ensure_ascii=False)
    return 4 + math.ceil(len(text) / 4)


def count_messages(messages: list[dict]) -> int:
    return sum(count_tokens(m) for m in messages)
