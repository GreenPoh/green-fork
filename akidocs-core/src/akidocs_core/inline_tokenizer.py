from akidocs_core.tokens import Bold, InlineText, Italic


def tokenize_inline(text: str) -> list[InlineText]:
    tokens = []
    current = ""
    i = 0

    while i < len(text):
        # Check for bold+italic (***) first
        if text[i : i + 3] == "***":
            if current:
                tokens.append(InlineText(content=current))
                current = ""

            end = text.find("***", i + 3)
            if end != -1:
                tokens.append(
                    InlineText(
                        content=text[i + 3 : end], styles=frozenset({Bold(), Italic()})
                    )
                )
                i = end + 3
            else:
                current += text[i]
                i += 1
        # Check for bold (**)
        elif text[i : i + 2] == "**":
            if current:
                tokens.append(InlineText(content=current))
                current = ""

            end = text.find("**", i + 2)
            if end != -1:
                tokens.append(
                    InlineText(content=text[i + 2 : end], styles=frozenset({Bold()}))
                )
                i = end + 2
            else:
                current += text[i]
                i += 1
        # Check for italic (*)
        elif text[i] == "*":
            if current:
                tokens.append(InlineText(content=current))
                current = ""

            end = text.find("*", i + 1)
            if end != -1:
                tokens.append(
                    InlineText(content=text[i + 1 : end], styles=frozenset({Italic()}))
                )
                i = end + 1
            else:
                current += text[i]
                i += 1
        else:
            current += text[i]
            i += 1

    if current:
        tokens.append(InlineText(content=current))

    return tokens
