import flet as ft

from app.core.config import APP_NAME
from app.ui.layouts.main_layout import MainLayout


class TranslateApp:

    def __init__(self, page: ft.Page):

        self.page = page

        self.configure()

        self.load_ui()

    def configure(self):

        self.page.title = APP_NAME

        self.page.window.width = 1400

        self.page.window.height = 850

        # Comenzaremos directamente en modo oscuro
        self.page.theme_mode = ft.ThemeMode.DARK

        self.page.padding = 0

        self.page.spacing = 0

        # Permitirá que la interfaz se adapte al tamaño de la ventana
        self.page.window.min_width = 900
        self.page.window.min_height = 600

    def load_ui(self):

        self.page.clean()

        self.page.add(
            MainLayout()
        )

        self.page.update()