import flet as ft


class StatusBar(ft.Container):

    def __init__(
        self,
        status_text: ft.Text,
    ):

        super().__init__(
            padding=10,
            content=ft.Row(
                controls=[
                    ft.Text(
                        "Estado:",
                        weight=ft.FontWeight.BOLD,
                    ),
                    status_text,
                ],
            ),
        )