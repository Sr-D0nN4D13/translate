from dataclasses import dataclass


@dataclass(frozen=True)
class ColorPalette:

    background: str

    surface: str

    card: str

    border: str

    primary: str

    text: str

    text_secondary: str

    hover: str


DARK = ColorPalette(

    background="#181818",

    surface="#222222",

    card="#2B2B2B",

    border="#3C3C3C",

    primary="#4F8CFF",

    text="#FFFFFF",

    text_secondary="#B8B8B8",

    hover="#343434",

)

LIGHT = ColorPalette(

    background="#F4F5F7",

    surface="#FFFFFF",

    card="#FFFFFF",

    border="#DADCE0",

    primary="#4F8CFF",

    text="#1A1A1A",

    text_secondary="#666666",

    hover="#ECECEC",

)