from dataclasses import dataclass


@dataclass
class TranslationRequest:
    text: str
    source_language: str
    target_language: str


@dataclass
class TranslationResult:
    translated_text: str