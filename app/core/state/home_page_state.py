from dataclasses import dataclass


@dataclass
class HomePageState:
    source_language: str = "auto"
    target_language: str = "en"

    detected_language: str = "auto"

    translating: bool = False

    correcting: bool = False