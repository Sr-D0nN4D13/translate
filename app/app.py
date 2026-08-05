import flet as ft

from app.core.config import AppConfig
from app.core.managers.theme_manager import ThemeManager
from app.ui.layouts.main_layout import MainLayout

class TranslateApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.theme_manager = ThemeManager(page)

        self.configure()
        self.theme_manager.apply()
        self.load()

    def configure(self):
        self.page.title = AppConfig.NAME
        self.page.padding = 0
        self.page.spacing = 0

        # Compatible con Desktop y futuras plataformas
        if self.page.window:
            self.page.window.width = AppConfig.WINDOW_WIDTH
            self.page.window.height = AppConfig.WINDOW_HEIGHT
            self.page.window.min_width = AppConfig.MIN_WIDTH
            self.page.window.min_height = AppConfig.MIN_HEIGHT

    def load(self):
        self.page.clean()
        self.page.add(
            MainLayout(
                page=self.page,
                theme_manager=self.theme_manager,
            )
        )