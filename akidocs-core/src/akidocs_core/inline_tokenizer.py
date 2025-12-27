from akidocs_core.tokens import Bold, InlineText, Italic, Style

DELIMITERS: list[tuple[str, frozenset[Style]]] = [
    ("***", frozenset({Bold(), Italic()})),
    ("**", frozenset({Bold()})),
    ("*", frozenset({Italic()})),
]


def _claimed_by_longer(text: str, delim: str, pos: int) -> bool:
    """Check if a longer delimiter claims this position."""
    for check_delim, _ in DELIMITERS:
        if len(check_delim) <= len(delim):
            continue
        if text[pos : pos + len(check_delim)] != check_delim:
            continue
        if _find_closing(text, check_delim, pos + len(check_delim)) != -1:
            return True
    return False


def _skip_nested_at(text: str, delim: str, pos: int) -> int | None:
    """If a different delimiter opens here and closes, return position after it."""
    for check_delim, _ in DELIMITERS:
        if check_delim == delim:
            continue
        if text[pos : pos + len(check_delim)] != check_delim:
            continue
        close = _find_closing(text, check_delim, pos + len(check_delim))
        if close != -1:
            return close + len(check_delim)
    return None


def _find_closing(text: str, delim: str, start: int) -> int:
    """Find closing delimiter, skipping nested sections."""
    i = start
    while i < len(text):
        if text[i : i + len(delim)] == delim:
            if not _claimed_by_longer(text, delim, i):
                return i

        skipped_to = _skip_nested_at(text, delim, i)
        if skipped_to is not None:
            i = skipped_to
        else:
            i += 1

    return -1


def tokenize_inline(
    text: str, inherited_styles: frozenset[Style] = frozenset()
) -> list[InlineText]:
    tokens: list[InlineText] = []
    text_buffer = ""
    i = 0

    while i < len(text):
        found_delimiter = False
        failed_opening_len = 0

        for delim, styles in DELIMITERS:
            if text[i : i + len(delim)] != delim:
                continue

            end = _find_closing(text, delim, i + len(delim))
            if end == -1:
                failed_opening_len = max(failed_opening_len, len(delim))
                continue

            # Reject if closer is within the range a longer delimiter claimed
            if end + len(delim) <= i + failed_opening_len:
                continue

            if text_buffer:
                tokens.append(InlineText(content=text_buffer, styles=inherited_styles))
                text_buffer = ""

            inner_content = text[i + len(delim) : end]
            combined_styles = inherited_styles | styles

            if inner_content:
                inner_tokens = tokenize_inline(inner_content, combined_styles)
                tokens.extend(inner_tokens)
            else:
                tokens.append(InlineText(content="", styles=combined_styles))

            i = end + len(delim)
            found_delimiter = True
            break

        if not found_delimiter:
            text_buffer += text[i]
            i += 1

    if text_buffer:
        tokens.append(InlineText(content=text_buffer, styles=inherited_styles))

    return tokens
