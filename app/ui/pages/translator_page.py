import flet as ft
from typing import Optional

from app.core.services.translation_service import TranslationService
from app.core.services.spell_checker import SpellCheckerService


class TranslatorPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self._page = page
        self.expand = True
        self.padding = 40
        
        # Inicializar servicios
        self.translation_service = None
        self.spell_checker_es = SpellCheckerService('es')
        self.spell_checker_en = SpellCheckerService('en')
        
        # Idiomas
        self.source_lang = "es"
        self.target_lang = "en"
        
        # Lista de idiomas disponibles
        self.languages = {
            "Español": "es",
            "English": "en",
            "Français": "fr",
            "Deutsch": "de",
            "Italiano": "it",
            "Português": "pt",
            "Русский": "ru",
            "中文": "zh",
            "日本語": "ja",
            "한국어": "ko",
            "العربية": "ar",
            "हिन्दी": "hi",
        }
        
        # Variables para controles
        self.source_text_field = None
        self.target_text_field = None
        self.source_dropdown = None
        self.target_dropdown = None
        self.copy_source_btn = None
        self.copy_target_btn = None
        self.translate_btn = None
        self.loading_indicator = None
        
        self._build_ui()
    
    def _build_ui(self):
        """Construye la interfaz del traductor"""
        
        # Dropdowns de idiomas
        self.source_dropdown = ft.Dropdown(
            label="Idioma origen",
            options=[ft.dropdown.Option(k, v) for k, v in self.languages.items()],
            value="Español",
            expand=True,
            on_change=self._on_language_change,
        )
        
        self.target_dropdown = ft.Dropdown(
            label="Idioma destino",
            options=[ft.dropdown.Option(k, v) for k, v in self.languages.items()],
            value="English",
            expand=True,
            on_change=self._on_language_change,
        )
        
        # Botón de intercambio
        swap_btn = ft.IconButton(
            icon=ft.Icons.SWAP_HORIZ,
            tooltip="Intercambiar idiomas",
            on_click=self._swap_languages,
        )
        
        # Campo de texto origen
        self.source_text_field = ft.TextField(
            label="Texto a traducir",
            multiline=True,
            min_lines=8,
            max_lines=12,
            expand=True,
            on_change=self._on_text_change,
        )
        
        # Botón de copiar origen con animación
        self.copy_source_btn = ft.ElevatedButton(
            content=ft.Row(
                tight=True,
                spacing=5,
                controls=[
                    ft.Icon(ft.Icons.COPY, size=18),
                    ft.Text("Copiar"),
                ]
            ),
            on_click=self._copy_source_text,
        )
        
        # Campo de texto destino
        self.target_text_field = ft.TextField(
            label="Traducción",
            multiline=True,
            min_lines=8,
            max_lines=12,
            expand=True,
            read_only=True,
        )
        
        # Botón de copiar destino con animación
        self.copy_target_btn = ft.ElevatedButton(
            content=ft.Row(
                tight=True,
                spacing=5,
                controls=[
                    ft.Icon(ft.Icons.COPY, size=18),
                    ft.Text("Copiar"),
                ]
            ),
            on_click=self._copy_target_text,
        )
        
        # Indicador de carga
        self.loading_indicator = ft.ProgressBar(
            indeterminate=True,
            visible=False,
        )
        
        # Botones de acción
        self.correct_btn = ft.ElevatedButton(
            "Corregir ortografía",
            icon=ft.Icons.SPELLCHECK,
            on_click=self._correct_spelling,
        )
        
        self.translate_btn = ft.FilledButton(
            "Traducir",
            icon=ft.Icons.TRANSLATE,
            on_click=self._translate_text,
        )
        
        # Ensamblar UI
        self.content = ft.Column(
            controls=[
                # Selector de idiomas
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.source_dropdown,
                        swap_btn,
                        self.target_dropdown,
                    ],
                ),
                
                ft.Divider(height=30),
                
                # Área de texto origen
                ft.Row(
                    controls=[
                        ft.Text("Texto original", weight=ft.FontWeight.BOLD),
                    ],
                ),
                self.source_text_field,
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[self.copy_source_btn],
                ),
                
                ft.Divider(height=20),
                
                # Indicador de carga
                self.loading_indicator,
                
                # Botones de acción
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                    controls=[
                        self.correct_btn,
                        self.translate_btn,
                    ],
                ),
                
                ft.Divider(height=20),
                
                # Área de texto destino
                ft.Row(
                    controls=[
                        ft.Text("Traducción", weight=ft.FontWeight.BOLD),
                    ],
                ),
                self.target_text_field,
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[self.copy_target_btn],
                ),
            ],
        )
    
    def _on_language_change(self, e):
        """Maneja el cambio de idioma"""
        if e.control == self.source_dropdown:
            self.source_lang = self.languages[self.source_dropdown.value]
        elif e.control == self.target_dropdown:
            self.target_lang = self.languages[self.target_dropdown.value]
    
    def _swap_languages(self, e):
        """Intercambia los idiomas origen y destino"""
        # Intercambiar valores
        self.source_lang, self.target_lang = self.target_lang, self.source_lang
        
        # Actualizar dropdowns
        source_name = [k for k, v in self.languages.items() if v == self.source_lang][0]
        target_name = [k for k, v in self.languages.items() if v == self.target_lang][0]
        
        self.source_dropdown.value = source_name
        self.target_dropdown.value = target_name
        
        # Intercambiar textos
        source_text = self.source_text_field.value
        target_text = self.target_text_field.value
        
        self.source_text_field.value = target_text
        self.target_text_field.value = source_text
        
        self._page.update()
    
    def _on_text_change(self, e):
        """Maneja cambios en el texto (para traducción automática futura)"""
        pass
    
    def _translate_text(self, e):
        """Realiza la traducción del texto"""
        text = self.source_text_field.value
        
        if not text.strip():
            self._show_snackbar("Ingresa un texto para traducir")
            return
        
        # Mostrar indicador de carga
        self.loading_indicator.visible = True
        self.translate_btn.disabled = True
        self._page.update()
        
        try:
            # Cargar modelo si no está cargado
            if self.translation_service is None:
                self.translation_service = TranslationService()
            
            # Traducir
            translation = self.translation_service.translate(
                text=text,
                source=self.source_lang,
                target=self.target_lang,
            )
            
            self.target_text_field.value = translation
            
        except Exception as ex:
            self._show_snackbar(f"Error en traducción: {str(ex)}")
        finally:
            # Ocultar indicador
            self.loading_indicator.visible = False
            self.translate_btn.disabled = False
            self._page.update()
    
    def _correct_spelling(self, e):
        """Corrige la ortografía del texto original"""
        text = self.source_text_field.value
        
        if not text.strip():
            self._show_snackbar("Ingresa un texto para corregir")
            return
        
        # Usar corrector según idioma origen
        if self.source_lang == 'es':
            corrected = self.spell_checker_es.correct(text)
        elif self.source_lang == 'en':
            corrected = self.spell_checker_en.correct(text)
        else:
            # Para otros idiomas usar español por defecto
            corrected = self.spell_checker_es.correct(text)
        
        self.source_text_field.value = corrected
        self._page.update()
        
        self._show_snackbar("Texto corregido")
    
    def _copy_source_text(self, e):
        """Copia el texto original al portapapeles con animación"""
        text = self.source_text_field.value
        
        if not text.strip():
            self._show_snackbar("No hay texto para copiar")
            return
        
        self._copy_to_clipboard(text, self.copy_source_btn)
    
    def _copy_target_text(self, e):
        """Copia el texto traducido al portapapeles con animación"""
        text = self.target_text_field.value
        
        if not text.strip():
            self._show_snackbar("No hay traducción para copiar")
            return
        
        self._copy_to_clipboard(text, self.copy_target_btn)
    
    def _copy_to_clipboard(self, text: str, btn: ft.ElevatedButton):
        """Copia texto al portapapeles y muestra animación en el botón"""
        # Copiar al portapapeles
        self._page.set_clipboard(text)
        
        # Guardar contenido original del botón
        original_content = btn.content
        
        # Cambiar a estado de éxito
        btn.content = ft.Row(
            tight=True,
            spacing=5,
            controls=[
                ft.Icon(ft.Icons.CHECK, size=18, color=ft.Colors.GREEN),
                ft.Text("¡Copiado!", color=ft.Colors.GREEN),
            ]
        )
        btn.disabled = True
        self._page.update()
        
        # Restaurar después de 2 segundos
        def restore_button():
            btn.content = original_content
            btn.disabled = False
            self._page.update()
        
        # Programar restauración usando timer de Flet
        self._page.overlay.append(
            ft.Control()  # Placeholder
        )
        self._page.update()
        
        # Usar threading para el delay
        import threading
        timer = threading.Timer(2.0, restore_button)
        timer.start()
        
        self._show_snackbar("Texto copiado al portapapeles")
    
    def _show_snackbar(self, message: str):
        """Muestra una notificación snackbar"""
        snackbar = ft.SnackBar(
            content=ft.Text(message),
            behavior=ft.SnackBarBehavior.FLOATING,
        )
        self._page.snack_bar = snackbar
        snackbar.open = True
        self._page.update()
