from tokenize import tokenize

from akidocs_core.inline_tokenizer import tokenize_inline

from akidocs_core.tokens import Italic, Text


def test_plain_text():
    result = tokenize_inline("hello world")
    assert result == [Text(content="hello world")]


def test_italic_only():
    result = tokenize_inline("*hello*")
    assert result == [Italic(content="hello")]


def test_text_then_italic():
    result = tokenize_inline("hello *world*")
    assert result == [Text(content="hello "), Italic(content="world")]
