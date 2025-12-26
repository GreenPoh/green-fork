from akidocs_core.tokens import Bold, InlineText, Italic, Style

DELIMITERS: list[tuple[str, frozenset[Style]]] = [
    ("***", frozenset({Bold(), Italic()})),
    ("**", frozenset({Bold()})),
    ("*", frozenset({Italic()})),
]


def _try_parse_styled(text: str, pos: int) -> tuple[InlineText, int] | None:
    """Try to parse a styled span starting at pos.

    Returns (token, new_position) if a complete styled span is found, None otherwise.
    Tries delimiters in order (longest first).
    """
    for delim, styles in DELIMITERS:
        if text[pos : pos + len(delim)] != delim:
            continue

        end = text.find(delim, pos + len(delim))
        if end != -1:
            content = text[pos + len(delim) : end]
            return InlineText(content=content, styles=styles), end + len(delim)

        # Delimiter matched but no closing - don't try shorter delimiters
        return None

    return None


def tokenize_inline(text: str) -> list[InlineText]:
    tokens: list[InlineText] = []
    current = ""
    i = 0

    while i < len(text):
        result = _try_parse_styled(text, i)

        if result is not None:
            if current:
                tokens.append(InlineText(content=current))
                current = ""
            token, i = result
            tokens.append(token)
        else:
            current += text[i]
            i += 1

    if current:
        tokens.append(InlineText(content=current))

    return tokens
