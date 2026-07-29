import flet as ft


class AppBar(ft.Container):

    def __init__(self):

        super().__init__(

            height=70,

            padding=20,

            content=ft.Row(

                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                controls=[

                    ft.Text(

                        "Translate",

                        size=30,

                        weight=ft.FontWeight.BOLD,

                    ),

                    ft.Row(

                        controls=[

                            ft.TextButton("Texto"),

                            ft.TextButton("Imagen"),

                            ft.TextButton("Documentos"),

                            ft.TextButton("Voz"),

                        ]

                    ),

                    ft.IconButton(

                        icon=ft.Icons.DARK_MODE_ROUNDED

                    )

                ]

            )

        )