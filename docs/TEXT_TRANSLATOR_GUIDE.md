# Traductor de Texto - Sprint 1.2

## Funcionalidades Implementadas

### 1. Traducción Automática con Small100
- **Modelo**: facebook/mbart-large-50-many-to-many-mmt (Small100)
- **Funcionamiento**: Traducción offline sin necesidad de conexión a internet
- **Idiomas soportados**: 
  - Español (es_ES)
  - Inglés (en_XX)
  - Francés (fr_XX)
  - Alemán (de_DE)
  - Italiano (it_IT)
  - Portugués (pt_XX)
  - Ruso (ru_RU)
  - Chino (zh_CN)
  - Japonés (ja_XX)
  - Coreano (ko_KR)
  - Árabe (ar_AR)
  - Hindi (hi_IN)

### 2. Corrección Ortográfica (Similar a DeepL)
- **Librería**: pyspellchecker
- **Características**:
  - Corrige errores ortográficos comunes
  - Mantiene mayúsculas y puntuación
  - Soporte para español e inglés
  - Ejemplo: "ola comi esstas" → "hola como estas"

### 3. Botones de Copiar con Animación
- **Funcionalidad**: Copia todo el contenido de ambos campos
- **Animación**: 
  - El botón cambia a un check verde con texto "¡Copiado!"
  - Se restaura automáticamente después de 2 segundos
  - Feedback visual inmediato al usuario

### 4. Interfaz de Usuario
- **Selectores de idioma**: Dropdowns para origen y destino
- **Botón de intercambio**: Intercambia idiomas y textos
- **Áreas de texto**: 
  - Campo editable para texto original
  - Campo de solo lectura para traducción
- **Indicador de carga**: Barra de progreso durante la traducción
- **Notificaciones**: Snackbars para feedback al usuario

### 5. Sin Historial
- **Privacidad**: No se guarda ningún historial de traducciones
- **Cada sesión**: Comienza limpia sin datos previos

## Estructura del Proyecto

```
app/
├── core/
│   ├── services/
│   │   ├── translation_service.py    # Servicio de traducción Small100
│   │   └── spell_checker.py          # Servicio de corrección ortográfica
├── ui/
│   ├── pages/
│   │   └── translator_page.py        # Página del traductor
│   ├── components/
│   │   └── app_bar.py                # Barra de navegación
│   └── layouts/
│       └── main_layout.py            # Layout principal
```

## Uso

### Traducción de Texto
1. Seleccionar idioma origen y destino
2. Escribir o pegar texto en el campo "Texto a traducir"
3. Click en "Traducir" o usar el botón de intercambio
4. Ver resultado en el campo "Traducción"

### Corrección Ortográfica
1. Escribir texto con posibles errores
2. Click en "Corregir ortografía"
3. El texto se corrige automáticamente

### Copiar Texto
1. Click en botón "Copiar" debajo de cada campo
2. El botón muestra animación de éxito
3. Texto disponible en portapapeles

## Dependencias

```toml
flet>=0.86.4
transformers>=4.35.0
torch>=2.0.0
sentencepiece>=0.1.99
sacremoses>=0.0.43
pyspellchecker>=0.7.2
```

## Notas Técnicas

- **Modelo de traducción**: Se carga una sola vez usando patrón Singleton
- **Primera traducción**: Puede tardar unos segundos mientras carga el modelo
- **Traducciones posteriores**: Más rápidas una vez cargado el modelo
- **Offline**: Todo funciona sin conexión a internet después de cargar el modelo
