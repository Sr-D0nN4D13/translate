import flet as ft

from app.core.managers.theme_manager import ThemeManager
from app.ui.components.app_bar import AppBar
from app.ui.pages.home_page import HomePage
from app.ui.pages.translator_page import TranslatorPage


class MainLayout(ft.Column):
    def __init__(
        self,
        page: ft.Page,
        theme_manager: ThemeManager,
    ):
        self.page = page
        self.theme_manager = theme_manager
        self.current_page = "texto"
        
        # Inicializar páginas
        self.home_page = HomePage()
        self.translator_page = TranslatorPage(page)
        
        super().__init__(
            expand=True,
            spacing=0,
            controls=[
                AppBar(
                    page=page,
                    theme_manager=theme_manager,
                    on_navigate=self._on_navigate,
                ),
                self.translator_page,  # Mostrar traductor por defecto
            ],
        )
    
    def _on_navigate(self, mode: str):
        """Maneja la navegación entre diferentes modos"""
        self.current_page = mode
        
        # Por ahora solo implementamos el modo texto
        if mode == "texto":
            self.controls[1] = self.translator_page
        elif mode == "imagen":
            self.controls[1] = ft.Container(
                expand=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.IMAGE, size=64),
                        ft.Text("Modo Imagen - Próximamente"),
                    ]
                )
            )
        elif mode == "documentos":
            self.controls[1] = ft.Container(
                expand=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.DESCRIPTION, size=64),
                        ft.Text("Modo Documentos - Próximamente"),
                    ]
                )
            )
        elif mode == "voz":
            self.controls[1] = ft.Container(
                expand=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.MIC, size=64),
                        ft.Text("Modo Voz - Próximamente"),
                    ]
                )
            )
        
        self.page.update()