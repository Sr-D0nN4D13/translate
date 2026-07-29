import flet as ft

from app.core.managers.theme_manager import ThemeManager


class AppBar(ft.Container):

    def __init__(self, page: ft.Page):

        self._page = page

        self.theme_manager = ThemeManager(page)

        super().__init__(

            height=72,

            padding=20,

            border=ft.border.only(
                bottom=ft.BorderSide(
                    1,
                    ft.Colors.OUTLINE_VARIANT,
                )
            ),

            content=ft.Row(

                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                vertical_alignment=ft.CrossAxisAlignment.CENTER,

                controls=[

                    ft.Text(
                        "Translate",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                    ),

                    ft.Row(
                        spacing=10,
                        controls=[
                            ft.TextButton("Texto"),
                            ft.TextButton("Imagen"),
                            ft.TextButton("Documentos"),
                            ft.TextButton("Voz"),
                        ],
                    ),

                    ft.IconButton(
                        icon=ft.Icons.DARK_MODE_ROUNDED,
                        tooltip="Cambiar tema",
                        on_click=self.change_theme,
                    ),

                ],

            ),

        )

    def change_theme(self, e):

        self.theme_manager.toggle()