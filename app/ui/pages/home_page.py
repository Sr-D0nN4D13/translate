import flet as ft

class HomePage(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            padding=40,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Bienvenido a Translate",
                        size=34,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Sprint 1.1 funcionando correctamente",
                        size=18,
                    )
                ]
            )
        )