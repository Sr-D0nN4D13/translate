import flet as ft


class ThemeManager:

    def __init__(self, page: ft.Page):

        self.page = page

    def apply(self):

        self.page.theme_mode = ft.ThemeMode.DARK

        self.page.theme = ft.Theme(
            color_scheme_seed=ft.Colors.BLUE,
            use_material3=True,
        )

        self.page.dark_theme = ft.Theme(
            color_scheme_seed=ft.Colors.BLUE,
            use_material3=True,
        )

    def toggle(self):

        if self.page.theme_mode == ft.ThemeMode.DARK:

            self.page.theme_mode = ft.ThemeMode.LIGHT

        else:

            self.page.theme_mode = ft.ThemeMode.DARK

        self.page.update()