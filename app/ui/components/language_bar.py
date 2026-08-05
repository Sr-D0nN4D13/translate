import flet as ft


class LanguageBar(ft.Container):

    def __init__(
        self,
        detected_language: ft.Text,
        swap_button: ft.IconButton,
        target_language: ft.Dropdown,
    ):

        super().__init__(
            padding=10,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    detected_language,
                    swap_button,
                    target_language,
                ],
            ),
        )