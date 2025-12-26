from dataclasses import dataclass


class Style:
    """Marker base class for inline styles."""

    pass


@dataclass(frozen=True)
class Bold(Style):
    pass


@dataclass(frozen=True)
class Italic(Style):
    pass


@dataclass
class InlineText:
    content: str
    styles: frozenset[Style] = frozenset()


@dataclass
class Header:
    level: int
    content: list[InlineText]


@dataclass
class Paragraph:
    content: list[InlineText]


Token = Header | Paragraph
