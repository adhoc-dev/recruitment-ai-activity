from chat.tokens import count_messages

CONTEXT_LIMIT = 8_000


class ContextLengthExceeded(Exception):
    pass


class InvalidRequest(Exception):
    pass


def send(messages: list[dict]) -> str:
    total = count_messages(messages)
    if total > CONTEXT_LIMIT:
        raise ContextLengthExceeded(
            f"This model's maximum context length is {CONTEXT_LIMIT} tokens. "
            f"However, your messages resulted in {total} tokens."
        )
    _check_tool_messages(messages)
    return "ok"


def _check_tool_messages(messages: list[dict]) -> None:
    pending: set[str] = set()
    for i, msg in enumerate(messages):
        if msg["role"] == "tool":
            call_id = msg.get("tool_call_id")
            if call_id not in pending:
                raise InvalidRequest(
                    f"messages[{i}]: messages with role 'tool' must be a response "
                    f"to a preceding message with 'tool_calls' (tool_call_id={call_id!r})."
                )
            pending.discard(call_id)
            continue
        if pending:
            raise InvalidRequest(
                f"messages[{i}]: an assistant message with 'tool_calls' must be "
                f"followed by tool messages responding to each 'tool_call_id' "
                f"(missing: {sorted(pending)})."
            )
        if msg["role"] == "assistant" and not msg.get("content") and not msg.get("tool_calls"):
            raise InvalidRequest(
                f"messages[{i}]: 'content' is required unless 'tool_calls' is specified."
            )
        if msg["role"] == "assistant" and msg.get("tool_calls"):
            pending = {call["id"] for call in msg["tool_calls"]}
    if pending:
        raise InvalidRequest(
            "an assistant message with 'tool_calls' must be followed by tool "
            f"messages responding to each 'tool_call_id' (missing: {sorted(pending)})."
        )
