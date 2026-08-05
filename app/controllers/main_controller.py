import flet as ft

from app.ui.pages.home_page import HomePage


class MainController:

    def __init__(
        self,
        page: ft.Page,
        view: HomePage,
    ):

        self.page = page
        self.view = view

        self._register_events()

    # =====================================================
    # REGISTRO DE EVENTOS
    # =====================================================

    def _register_events(self):

        self.view.swap_button.on_click = self._swap_languages

        self.view.copy_source_button.on_click = self._copy_source

        self.view.copy_translation_button.on_click = (
            self._copy_translation
        )

        self.view.source_text.on_change = (
            self._source_text_changed
        )

    # =====================================================
    # EVENTOS
    # =====================================================

    def _copy_source(self, e):

        text = self.view.get_source_text()

        if not text:

            return

        self.page.clipboard.set(text)

        self.view.set_status("Texto copiado.")

        self.view.refresh()

    def _copy_translation(self, e):

        text = self.view.get_translation()

        if not text:

            return

        self.page.clipboard.set(text)

        self.view.set_status("Traducción copiada.")

        self.view.refresh()

    def _swap_languages(self, e):

        source_text = self.view.get_source_text()

        translation = self.view.get_translation()

        self.view.swap_languages()

        self.view.set_source_text(translation)

        self.view.set_translation(source_text)

        self.view.set_status("Idiomas intercambiados.")

        self.view.refresh()

    def _source_text_changed(self, e):

        if self.view.get_source_text().strip() == "":

            self.view.clear_translation()

            self.view.set_status("Esperando entrada...")

            self.view.refresh()

            return

        #
        # Aquí comenzará el pipeline de IA.
        #

        self.view.set_status("Preparando traducción...")

        self.view.refresh()