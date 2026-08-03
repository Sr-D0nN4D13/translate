# Guía de Instalación y Ejecución - Traductor Offline

## Requisitos del Sistema

- **Python**: 3.11 o superior (recomendado 3.11.15)
- **RAM**: Mínimo 4GB (8GB recomendado para cargar modelos)
- **Espacio en disco**: ~5GB para modelos de traducción
- **Sistema Operativo**: Windows, macOS o Linux

## Instalación Paso a Paso

### 1. Clonar o Descargar el Proyecto

```bash
git clone <tu-repositorio-github>
cd translate
```

### 2. Crear Entorno Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

O instalar manualmente:

```bash
pip install flet>=0.86.4
pip install transformers>=4.35.0
pip install torch>=2.0.0
pip install sentencepiece>=0.1.99
pip install sacremoses>=0.0.43
pip install pyspellchecker>=0.7.2
```

### 4. Ejecutar la Aplicación

```bash
python main.py
```

**Nota importante**: La primera ejecución descargará automáticamente el modelo de traducción (~2.5GB). Esto puede tomar varios minutos dependiendo de tu conexión a internet. Las siguientes ejecuciones usarán el modelo en caché.

## Estructura del Proyecto

```
translate/
├── main.py                 # Punto de entrada principal
├── pyproject.toml          # Configuración del proyecto
├── requirements.txt        # Dependencias
├── README.md              # Documentación principal
├── app/
│   ├── app.py             # Clase principal de la aplicación
│   ├── core/
│   │   ├── config.py      # Configuración global
│   │   ├── services/
│   │   │   ├── translation_service.py  # Servicio Small100
│   │   │   ├── spell_checker.py        # Corrector ortográfico
│   │   │   ├── ocr_service.py          # OCR para cámara
│   │   │   └── voice_service.py        # Reconocimiento de voz
│   │   └── managers/
│   │       └── theme_manager.py        # Tema claro/oscuro
│   ├── ui/
│   │   ├── layouts/
│   │   │   └── main_layout.py          # Layout principal
│   │   ├── pages/
│   │   │   ├── translator_page.py      # Página de traducción
│   │   │   └── home_page.py            # Página de inicio
│   │   └── components/
│   │       └── app_bar.py              # Barra de navegación
│   └── features/
│       ├── translation/     # Funcionalidades de traducción
│       ├── ocr/            # Funcionalidades OCR
│       ├── documents/      # Traducción de documentos
│       └── voice/          # Traducción por voz
└── docs/
    ├── ARCHITECTURE.md     # Arquitectura del sistema
    ├── TEXT_TRANSLATOR_GUIDE.md  # Guía del traductor de texto
    └── ROADMAP.md          # Hoja de ruta
```

## Características Implementadas

### ✅ Traductor de Texto (COMPLETO)
- **Traducción automática** con modelo Small100 (facebook/mbart-large-50-many-to-many-mmt)
- **Corrección ortográfica** similar a DeepL
- **12 idiomas soportados**: Español, Inglés, Francés, Alemán, Italiano, Portugués, Ruso, Chino, Japonés, Coreano, Árabe, Hindi
- **Botones de copiar** con animación de confirmación
- **Intercambio de idiomas** con un clic
- **Sin historial** - privacidad garantizada
- **Funcionamiento 100% offline** después de la primera descarga

### 🚧 En Desarrollo
- Traducción por cámara (OCR)
- Traducción de documentos
- Traducción por voz

## Idiomas Soportados

| Código | Idioma | Código Small100 |
|--------|--------|-----------------|
| es | Español | es_ES |
| en | English | en_XX |
| fr | Français | fr_XX |
| de | Deutsch | de_DE |
| it | Italiano | it_IT |
| pt | Português | pt_XX |
| ru | Русский | ru_RU |
| zh | 中文 | zh_CN |
| ja | 日本語 | ja_XX |
| ko | 한국어 | ko_KR |
| ar | العربية | ar_AR |
| hi | हिन्दी | hi_IN |

## Solución de Problemas Comunes

### Error: "No module named 'transformers'"
```bash
pip install --upgrade pip
pip install transformers
```

### Error: "CUDA out of memory" (si tienes GPU)
El modelo se ejecutará automáticamente en CPU si no hay suficiente memoria GPU.

### La aplicación no inicia en Linux
```bash
# Instalar dependencias del sistema
sudo apt-get update
sudo apt-get install python3-tk python3-dev
```

### Error al descargar el modelo
Verifica tu conexión a internet. El modelo se descarga de Hugging Face. Puedes descargarlo manualmente:

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
```

### La traducción es lenta
- La primera traducción es más lenta porque carga el modelo
- Las siguientes traducciones son más rápidas
- Considera usar una máquina con más RAM o GPU

## Uso Básico

1. **Iniciar la aplicación**: `python main.py`
2. **Seleccionar idiomas**: Usa los dropdowns para elegir idioma origen y destino
3. **Escribir texto**: Ingresa el texto en el campo "Texto a traducir"
4. **Corregir ortografía** (opcional): Haz clic en "Corregir ortografía"
5. **Traducir**: Haz clic en "Traducir"
6. **Copiar resultado**: Usa el botón "Copiar" en cualquiera de los campos

## Atajos y Funciones

- **Intercambiar idiomas**: Botón con ícono de flechas entre los selectores
- **Copiar texto**: Botones "Copiar" con animación de confirmación
- **Cambiar tema**: Botón de luna/sol en la barra superior
- **Navegación**: Pestañas superiores para cambiar entre modos (Texto, Imagen, Documentos, Voz)

## Publicar en GitHub

Antes de publicar:

1. **Crear .gitignore** (ya incluido):
   ```
   __pycache__/
   *.pyc
   .env
   venv/
   *.log
   .DS_Store
   ```

2. **Inicializar repositorio**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Offline translator with Small100"
   ```

3. **Subir a GitHub**:
   ```bash
   git remote add origin https://github.com/tu-usuario/traductor-offline.git
   git branch -M main
   git push -u origin main
   ```

4. **Actualizar README.md** con instrucciones claras

5. **Agregar licencia** (MIT, Apache 2.0, etc.)

## Próximos Pasos

1. ✅ Traductor de texto (COMPLETADO)
2. 🔄 Traducción por cámara (OCR)
3. 🔄 Traducción de documentos (PDF, DOCX)
4. 🔄 Traducción por voz (STT + TTS)
5. 🔄 Empaquetado para móviles (Android/iOS)

## Contacto y Contribución

Para contribuir al proyecto:
1. Fork del repositorio
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de cambios (`git commit -m 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abrir Pull Request

---

**Nota**: Este proyecto funciona completamente offline después de la primera descarga de modelos. No se envían datos a servidores externos.
