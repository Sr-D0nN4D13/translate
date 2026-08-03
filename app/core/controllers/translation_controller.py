from app.core.services.translation_service import TranslationService
from app.core.state.app_state import AppState


class TranslationController:

    def __init__(self, state: AppState):
        self.state = state
        self.service = TranslationService()

    def translate(self):
        if not self.state.input_text.strip():
            return

        self.state.translated_text = self.service.translate(
            self.state.input_text,
            self.state.source_language,
            self.state.target_language,
        )