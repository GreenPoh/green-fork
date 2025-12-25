from akidocs_core.renderer import render_pdf
from akidocs_core.tokens import Header, Paragraph


def test_render_returns_bytes():
    tokens = [Paragraph(content="Hello")]
    result = render_pdf(tokens)
    assert isinstance(result, bytes)
    assert len(result) > 0


def test_render_handles_headers():
    tokens = [Header(level=1, content="Title"), Paragraph(content="Body text")]
    result = render_pdf(tokens)
    assert isinstance(result, bytes)
    assert len(result) > 0
