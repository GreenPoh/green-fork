from akidocs_core.renderer import render_pdf
from akidocs_core.tokens import Bold, Header, InlineText, Italic, Paragraph


def assert_valid_pdf_bytes(result: bytes) -> None:
    """Assert that result is non-empty PDF bytes."""
    assert isinstance(result, bytes)
    assert len(result) > 0


def test_render_returns_bytes():
    tokens = [Paragraph(content=[InlineText(content="Hello")])]
    result = render_pdf(tokens)
    assert isinstance(result, bytes)
    assert len(result) > 0


def test_render_handles_headers():
    tokens = [
        Header(level=1, content=[InlineText(content="Title")]),
        Paragraph(content=[InlineText(content="Body text")]),
    ]
    result = render_pdf(tokens)
    assert_valid_pdf_bytes(result)


def test_render_handles_italic():
    tokens = [
        Paragraph(
            content=[
                InlineText(content="hello "),
                InlineText(content="world", styles=frozenset({Italic()})),
            ]
        )
    ]
    result = render_pdf(tokens)
    assert_valid_pdf_bytes(result)


def test_render_handles_bold():
    tokens = [
        Paragraph(
            content=[
                InlineText(content="hello "),
                InlineText(content="world", styles=frozenset({Bold()})),
            ]
        )
    ]
    result = render_pdf(tokens)
    assert_valid_pdf_bytes(result)
