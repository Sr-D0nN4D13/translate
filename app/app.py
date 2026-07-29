import flet as ft

from app.core.config import APP_NAME


class TranslateApp:

    def __init__(self, page: ft.Page):

        self.page = page

        self.configure()

    def configure(self):

        self.page.title = APP_NAME

        self.page.window.width = 1400

        self.page.window.height = 850

        self.page.theme_mode = ft.ThemeMode.SYSTEM

        self.page.padding = 0

        self.page.spacing = 0