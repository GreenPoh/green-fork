from dataclasses import dataclass


@dataclass
class Header:
    level: int
    content: str


@dataclass
class Paragraph:
    content: str


Token = Header | Paragraph
