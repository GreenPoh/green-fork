from akidocs_core.inline_tokenizer import tokenize_inline
from akidocs_core.tokens import Bold, InlineText, Italic


def test_plain_text():
    result = tokenize_inline("hello world")
    assert result == [InlineText(content="hello world")]


def test_italic_only():
    result = tokenize_inline("*hello*")
    assert result == [InlineText(content="hello", styles=frozenset({Italic()}))]


def test_text_then_italic():
    result = tokenize_inline("hello *world*")
    assert result == [
        InlineText(content="hello "),
        InlineText(content="world", styles=frozenset({Italic()})),
    ]


def test_bold_only():
    result = tokenize_inline("**hello**")
    assert result == [InlineText(content="hello", styles=frozenset({Bold()}))]


def test_text_then_bold():
    result = tokenize_inline("hello **world**")
    assert result == [
        InlineText(content="hello "),
        InlineText(content="world", styles=frozenset({Bold()})),
    ]


def test_bold_italic():
    result = tokenize_inline("***hello***")
    assert len(result) == 1
    assert result[0].content == "hello"
    assert Bold() in result[0].styles
    assert Italic() in result[0].styles
