from app.ui.components.app_bar import AppBar

from app.ui.pages.home_page import HomePage

import flet as ft


class MainLayout(ft.Column):

    def __init__(self):

        super().__init__(

            expand=True,

            spacing=0,

            controls=[

                AppBar(),

                HomePage()

            ]

        )