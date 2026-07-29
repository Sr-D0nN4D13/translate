import flet as ft


class HomePage(ft.Container):

    def __init__(self):

        super().__init__(

            expand=True,

            alignment=ft.Alignment(0, 0),

            content=ft.Text(

                "Bienvenido a Translate",

                size=24,

                weight=ft.FontWeight.BOLD,

            )

        )