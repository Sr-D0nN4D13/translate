# 🌐 Translate - Traductor Offline IA

Traductor inteligente completamente offline para Windows, macOS, Linux y Android. Funciona sin conexión a internet después de la primera descarga de modelos.

## ✨ Características Principales

### ✅ Implementadas
- **📝 Traductor de Texto**: Traducción automática con corrección ortográfica integrada
- **🎯 Modelo Small100**: facebook/mbart-large-50-many-to-many-mmt
- **🔒 100% Offline**: Sin envío de datos a servidores externos
- **🎨 Interfaz Moderna**: UI/UX similar a DeepL con Flet
- **🌍 12 Idiomas**: Español, Inglés, Francés, Alemán, Italiano, Portugués, Ruso, Chino, Japonés, Coreano, Árabe, Hindi
- **📋 Copiado Rápido**: Botones con animación de confirmación
- **🌙 Tema Claro/Oscuro**: Cambia según tu preferencia

### 🚧 En Desarrollo
- 📷 Traducción por Cámara (OCR) - Similar a Google Lens
- 📄 Traductor de Documentos (PDF, DOCX, TXT)
- 🎤 Traducción por Voz (STT + TTS en tiempo real)
- 📱 Versión Móvil para Android/iOS

## 🚀 Inicio Rápido

### Prerrequisitos
- Python 3.11 o superior
- 4GB RAM mínimo (8GB recomendado)
- 5GB espacio en disco para modelos

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/traductor-offline.git
cd traductor-offline

# Crear entorno virtual
python -m venv venv

# Activar entorno
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python main.py
```

**⚠️ Nota**: La primera ejecución descargará el modelo (~2.5GB). Las siguientes ejecuciones serán más rápidas.

## 💻 Uso

1. **Iniciar**: Ejecuta `python main.py`
2. **Seleccionar idiomas**: Elige idioma origen y destino
3. **Escribir texto**: Ingresa el texto a traducir
4. **Corregir** (opcional): Usa "Corregir ortografía" para errores
5. **Traducir**: Presiona "Traducir"
6. **Copiar**: Usa los botones "Copiar" con animación

### Ejemplo de Corrección Ortográfica
```
Entrada:  "ola comi esstas"
Corrección: "ola como estas"
Traducción: "hello how are you"
```

## 📁 Estructura del Proyecto

```
traductor-offline/
├── main.py                    # Punto de entrada
├── requirements.txt           # Dependencias
├── README.md                  # Esta documentación
├── app/
│   ├── app.py                # Aplicación principal
│   ├── core/
│   │   ├── config.py         # Configuración
│   │   ├── services/
│   │   │   ├── translation_service.py  # Small100
│   │   │   └── spell_checker.py        # Corrector
│   │   └── managers/
│   │       └── theme_manager.py        # Temas
│   └── ui/
│       ├── layouts/
│       ├── pages/
│       └── components/
└── docs/                     # Documentación adicional
```

## 🌍 Idiomas Soportados

| Idioma | Código | | Idioma | Código |
|--------|--------|-|--------|--------|
| Español | es | | Italiano | it |
| English | en | | Português | pt |
| Français | fr | | Русский | ru |
| Deutsch | de | | 中文 | zh |
| العربية | ar | | 日本語 | ja |
| हिन्दी | hi | | 한국어 | ko |

## 🔧 Solución de Problemas

### Error al importar módulos
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Error de memoria (GPU)
El modelo usa CPU automáticamente si no hay suficiente VRAM.

### Primera ejecución lenta
Es normal mientras descarga el modelo de Hugging Face (~2.5GB).

## 📋 Roadmap

- [x] Traductor de texto con Small100
- [x] Corrector ortográfico tipo DeepL
- [x] Interfaz con Flet
- [ ] OCR para traducción por cámara
- [ ] Traductor de documentos (PDF, DOCX)
- [ ] Reconocimiento de voz (STT)
- [ ] Síntesis de voz (TTS)
- [ ] App móvil Android
- [ ] App móvil iOS

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## ⚠️ Importante

- **Privacidad**: Todo el procesamiento es local, nada se envía a internet
- **Offline**: Después de la primera descarga, funciona sin conexión
- **Rendimiento**: La primera traducción es más lenta (carga del modelo)

---

**Hecho con ❤️ usando Python y Flet**
