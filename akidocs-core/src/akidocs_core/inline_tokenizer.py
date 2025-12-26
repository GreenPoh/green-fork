from akidocs_core.tokens import Bold, InlineText, Italic, Style

DELIMITERS: list[tuple[str, frozenset[Style]]] = [
    ("***", frozenset({Bold(), Italic()})),
    ("**", frozenset({Bold()})),
    ("*", frozenset({Italic()})),
]


def _find_closing(text: str, delim: str, start: int) -> int:
    """Find closing delimiter, skipping nested sections."""
    i = start
    while i < len(text):
        if text[i : i + len(delim)] == delim:
            longer_valid = False
            for check_delim, _ in DELIMITERS:
                if len(check_delim) <= len(delim):
                    continue
                if text[i : i + len(check_delim)] != check_delim:
                    continue
                close = _find_closing(text, check_delim, i + len(check_delim))
                if close != -1:
                    longer_valid = True
                    break

            if not longer_valid:
                return i

        skipped = False
        for check_delim, _ in DELIMITERS:
            if check_delim == delim:
                continue
            if text[i : i + len(check_delim)] != check_delim:
                continue

            close = _find_closing(text, check_delim, i + len(check_delim))
            if close != -1:
                i = close + len(check_delim)
                skipped = True
                break

        if not skipped:
            i += 1

    return -1


def tokenize_inline(
    text: str, inherited_styles: frozenset[Style] = frozenset()
) -> list[InlineText]:
    tokens: list[InlineText] = []
    current = ""
    i = 0

    while i < len(text):
        matched = False
        longest_failed = 0

        for delim, styles in DELIMITERS:
            if text[i : i + len(delim)] != delim:
                continue

            end = _find_closing(text, delim, i + len(delim))
            if end == -1:
                longest_failed = max(longest_failed, len(delim))
                continue

            # Reject if closer is within the range a longer delimiter claimed
            if end + len(delim) <= i + longest_failed:
                continue

            if current:
                tokens.append(InlineText(content=current, styles=inherited_styles))
                current = ""

            inner_content = text[i + len(delim) : end]
            combined_styles = inherited_styles | styles

            if inner_content:
                inner_tokens = tokenize_inline(inner_content, combined_styles)
                tokens.extend(inner_tokens)
            else:
                tokens.append(InlineText(content="", styles=combined_styles))

            i = end + len(delim)
            matched = True
            break

        if not matched:
            current += text[i]
            i += 1

    if current:
        tokens.append(InlineText(content=current, styles=inherited_styles))

    return tokens
