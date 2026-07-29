import flet as ft

from app.ui.components.app_bar import AppBar
from app.ui.pages.home_page import HomePage


class MainLayout(ft.Column):

    def __init__(self, page: ft.Page):

        super().__init__(

            expand=True,

            spacing=0,

            controls=[

                AppBar(page),

                HomePage(),

            ]

        )