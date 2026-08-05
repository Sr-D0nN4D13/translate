import flet as ft


class SourcePanel(ft.Container):

    def __init__(
        self,
        title: str,
        copy_button: ft.IconButton,
        textfield: ft.TextField,
    ):

        super().__init__(
            expand=True,
            padding=10,
            content=ft.Column(
                expand=True,
                spacing=10,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                title,
                                weight=ft.FontWeight.BOLD,
                            ),
                            copy_button,
                        ],
                    ),
                    textfield,
                ],
            ),
        )