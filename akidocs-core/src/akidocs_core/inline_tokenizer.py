from akidocs_core.tokens import Bold, InlineText, Italic, Style

DELIMITERS: list[tuple[str, frozenset[Style]]] = [
    ("***", frozenset({Bold(), Italic()})),
    ("**", frozenset({Bold()})),
    ("*", frozenset({Italic()})),
]


def tokenize_inline(
    text: str, inherited_styles: frozenset[Style] = frozenset()
) -> list[InlineText]:
    tokens: list[InlineText] = []
    current = ""
    i = 0

    while i < len(text):
        matched = False

        for delim, styles in DELIMITERS:
            if text[i : i + len(delim)] != delim:
                continue

            end = text.find(delim, i + len(delim))
            if end == -1:
                break

            if current:
                tokens.append(InlineText(content=current, styles=inherited_styles))
                current = ""

            inner_content = text[i + len(delim) : end]
            combined_styles = inherited_styles | styles
            inner_tokens = tokenize_inline(inner_content, combined_styles)
            tokens.extend(inner_tokens)

            i = end + len(delim)
            matched = True
            break

        if not matched:
            current += text[i]
            i += 1

    if current:
        tokens.append(InlineText(content=current, styles=inherited_styles))

    return tokens
