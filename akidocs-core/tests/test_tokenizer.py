from akidocs_core.tokenizer import tokenize


def test_empty_string_returns_empty_list():
    assert tokenize("") == []


def test_plain_paragraph():
    result = tokenize("Hello world")
    assert len(result) == 1
    assert result[0]["type"] == "paragraph"
    assert result[0]["content"] == "Hello world"
