import flet as ft

from app.core.managers.theme_manager import ThemeManager
from app.ui.components.app_bar import AppBar
from app.ui.pages.home_page import HomePage


class MainLayout(ft.Column):
    def __init__(
        self,
        page: ft.Page,
        theme_manager: ThemeManager,
    ):
        super().__init__(
            expand=True,
            spacing=0,
            controls=[
                AppBar(
                    page=page,
                    theme_manager=theme_manager,
                ),
                HomePage(),
            ],
        )