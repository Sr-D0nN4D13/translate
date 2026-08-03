from dataclasses import dataclass, field


@dataclass
class AppState:
    source_language: str = "es"
    target_language: str = "en"

    input_text: str = ""
    translated_text: str = ""

    selected_model: str | None = None

    current_page: str = "home"

    is_loading: bool = False

    history: list = field(default_factory=list)