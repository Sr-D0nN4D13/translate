import flet as ft

from app.core.managers.theme_manager import ThemeManager


class AppBar(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        theme_manager: ThemeManager,
        on_navigate=None,
    ):
        self._page = page
        self.theme_manager = theme_manager
        self.on_navigate = on_navigate
        
        # Estado del botón activo
        self.active_mode = "texto"

        super().__init__(
            height=72,
            padding=20,
            border=ft.Border.only(
                bottom=ft.BorderSide(
                    width=1,
                    color=ft.Colors.OUTLINE_VARIANT,
                )
            ),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Translate",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Row(
                        spacing=10,
                        controls=[
                            self._create_nav_button("Texto", "texto"),
                            self._create_nav_button("Imagen", "imagen"),
                            self._create_nav_button("Documentos", "documentos"),
                            self._create_nav_button("Voz", "voz"),
                        ],
                    ),
                    ft.IconButton(
                        icon=ft.Icons.DARK_MODE_ROUNDED,
                        tooltip="Cambiar tema",
                        on_click=self.change_theme,
                    ),
                ],
            ),
        )
    
    def _create_nav_button(self, text: str, mode: str):
        """Crea un botón de navegación con estilo dinámico"""
        return ft.TextButton(
            text,
            data=mode,
            style=ft.ButtonStyle(
                overlay_color=ft.Colors.TRANSPARENT,
            ),
            on_click=self._on_navigate,
        )
    
    def _on_navigate(self, e):
        """Maneja la navegación entre modos"""
        mode = e.control.data
        
        if mode == self.active_mode:
            return
        
        self.active_mode = mode
        
        # Actualizar estilos de botones
        for control in self.content.controls[1].controls:
            if control.data == mode:
                control.style = ft.ButtonStyle(
                    bgcolor=ft.Colors.PRIMARY_CONTAINER,
                    shape=ft.RoundedRectangleBorder(radius=8),
                )
            else:
                control.style = ft.ButtonStyle(
                    overlay_color=ft.Colors.TRANSPARENT,
                )
        
        self._page.update()
        
        # Notificar cambio de página
        if self.on_navigate:
            self.on_navigate(mode)

    def change_theme(self, e):
        self.theme_manager.toggle()