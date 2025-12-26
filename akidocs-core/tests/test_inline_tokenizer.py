from tokenize import tokenize

from akidocs_core.inline_tokenizer import tokenize_inline
from akidocs_core.tokens import Bold, Italic, Text


def test_plain_text():
    result = tokenize_inline("hello world")
    assert result == [Text(content="hello world")]


def test_italic_only():
    result = tokenize_inline("*hello*")
    assert result == [Italic(content="hello")]


def test_text_then_italic():
    result = tokenize_inline("hello *world*")
    assert result == [Text(content="hello "), Italic(content="world")]


def test_bold_only():
    result = tokenize_inline("**hello**")
    assert result == [Bold(content="hello")]


def test_text_then_bold():
    result = tokenize_inline("hello **world**")
    assert result == [Text(content="hello "), Bold(content="world")]


def test_bold_italic():
    result = tokenize_inline("***hello***")
    assert len(result) == 1
    assert result[0].content == "hello"
    assert Bold() in result[0].styles
    assert Italic() in result[0].styles
