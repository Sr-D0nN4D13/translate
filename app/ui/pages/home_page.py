import flet as ft

from app.core.constants.languages import LANGUAGES
from app.core.state.home_page_state import HomePageState

from app.ui.components.language_bar import LanguageBar
from app.ui.components.source_panel import SourcePanel
from app.ui.components.translation_panel import TranslationPanel
from app.ui.components.status_bar import StatusBar


class HomePage(ft.Container):

    def __init__(self):

        self.state = HomePageState()

        self._create_controls()

        super().__init__(
            expand=True,
            padding=20,
            content=self._build_ui(),
        )

        self.refresh_languages()

    # ==========================================================
    # CREACIÓN DE CONTROLES
    # ==========================================================

    def _create_controls(self):

        self.detected_language = ft.Text(
            size=16,
            weight=ft.FontWeight.W_500,
        )

        self.swap_button = ft.IconButton(
            icon=ft.Icons.SWAP_HORIZ,
            tooltip="Intercambiar idiomas",
        )

        self.target_language = ft.Dropdown(
            width=180,
            value=self.state.target_language,
            options=[
                ft.dropdown.Option(
                    key,
                    value["name"],
                )
                for key, value in LANGUAGES.items()
                if key != "auto"
            ],
        )

        self.source_text = ft.TextField(
            expand=True,
            multiline=True,
            min_lines=18,
            max_lines=18,
            hint_text="Escribe o pega el texto aquí...",
        )

        self.translation_text = ft.TextField(
            expand=True,
            multiline=True,
            min_lines=18,
            max_lines=18,
            read_only=True,
            hint_text="La traducción aparecerá aquí...",
        )

        self.copy_source_button = ft.IconButton(
            icon=ft.Icons.CONTENT_COPY,
            tooltip="Copiar texto",
        )

        self.copy_translation_button = ft.IconButton(
            icon=ft.Icons.CONTENT_COPY,
            tooltip="Copiar traducción",
        )

        self.status_text = ft.Text(
            "Listo",
            size=14,
        )

    # ==========================================================
    # INTERFAZ
    # ==========================================================

    def _build_ui(self):

        return ft.Column(
            expand=True,
            spacing=20,
            controls=[

                LanguageBar(
                    detected_language=self.detected_language,
                    swap_button=self.swap_button,
                    target_language=self.target_language,
                ),

                ft.ResponsiveRow(
                    expand=True,
                    spacing=20,
                    run_spacing=20,
                    controls=[

                        ft.Container(
                            col={
                                "sm": 12,
                                "md": 6,
                                "lg": 6,
                            },
                            content=SourcePanel(
                                title="Texto original",
                                copy_button=self.copy_source_button,
                                textfield=self.source_text,
                            ),
                        ),

                        ft.Container(
                            col={
                                "sm": 12,
                                "md": 6,
                                "lg": 6,
                            },
                            content=TranslationPanel(
                                title="Traducción",
                                copy_button=self.copy_translation_button,
                                textfield=self.translation_text,
                            ),
                        ),

                    ],
                ),

                StatusBar(
                    status_text=self.status_text,
                ),

            ],
        )

    # ==========================================================
    # API PÚBLICA
    # ==========================================================

    def get_source_text(self):

        return self.source_text.value or ""

    def set_source_text(self, text: str):

        self.source_text.value = text

    def clear_source_text(self):

        self.source_text.value = ""

    def get_translation(self):

        return self.translation_text.value or ""

    def set_translation(self, text: str):

        self.translation_text.value = text

    def clear_translation(self):

        self.translation_text.value = ""

    def set_status(self, text: str):

        self.status_text.value = text

    def get_source_language(self):

        return self.state.source_language

    def get_target_language(self):

        return self.state.target_language

    def set_source_language(self, code: str):

        self.state.source_language = code
        self.refresh_languages()

    def set_target_language(self, code: str):

        self.state.target_language = code
        self.target_language.value = code

    def swap_languages(self):

        self.state.source_language, self.state.target_language = (
            self.state.target_language,
            self.state.source_language,
        )

        self.target_language.value = self.state.target_language

        self.refresh_languages()

    # ==========================================================
    # ACTUALIZACIÓN DE LA INTERFAZ
    # ==========================================================

    def refresh_languages(self):

        source = self.state.source_language

        if source == "auto":

            self.detected_language.value = LANGUAGES["auto"]["name"]

        else:

            self.detected_language.value = LANGUAGES[source]["name"]
    # ==========================================================
    # ACTUALIZAR VISTA
    # ==========================================================

    def refresh(self):
        self.update()

    def update_view(self):
        self.update()