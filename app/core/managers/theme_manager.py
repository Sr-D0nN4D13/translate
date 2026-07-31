import flet as ft

from app.core.config import AppConfig


class ThemeManager:
    def __init__(self, page: ft.Page):
        self.page = page

    def apply(self):
        theme = ft.Theme(
            color_scheme_seed=ft.Colors.BLUE,
            use_material3=True,
        )

        self.page.theme = theme
        self.page.dark_theme = theme

        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if AppConfig.DEFAULT_THEME.lower() == "dark"
            else ft.ThemeMode.LIGHT
        )

    def toggle(self):
        self.page.theme_mode = (
            ft.ThemeMode.LIGHT
            if self.page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )

        self.page.update()