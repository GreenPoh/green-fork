from dataclasses import dataclass


class InlineStyle:
    """Marker base class for inline styles."""

    pass


@dataclass(frozen=True)
class Bold(InlineStyle):
    pass


@dataclass(frozen=True)
class Italic(InlineStyle):
    pass


@dataclass
class InlineText:
    content: str
    styles: frozenset[InlineStyle] = frozenset()


@dataclass
class Header:
    level: int
    content: list[InlineText]


@dataclass
class Paragraph:
    content: list[InlineText]


Token = Header | Paragraph
