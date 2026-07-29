import flet as ft

from app.core.config import AppConfig

from app.core.managers.theme_manager import ThemeManager

from app.ui.layouts.main_layout import MainLayout


class TranslateApp:

    def __init__(self, page: ft.Page):

        self.page = page

        self.configure()

        ThemeManager(page).apply()

        self.load()

    def configure(self):

        self.page.title = AppConfig.NAME

        self.page.window.width = AppConfig.WINDOW_WIDTH

        self.page.window.height = AppConfig.WINDOW_HEIGHT

        self.page.window.min_width = AppConfig.MIN_WIDTH

        self.page.window.min_height = AppConfig.MIN_HEIGHT

        self.page.padding = 0

        self.page.spacing = 0

    def load(self):

        self.page.clean()

        self.page.add(

            MainLayout(self.page)

        )

        self.page.update()