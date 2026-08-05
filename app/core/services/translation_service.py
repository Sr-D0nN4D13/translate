from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class TranslationService:
    _instance = None
    _model = None
    _tokenizer = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._model is None:
            self.load_model()

    def load_model(self):
        """Carga el modelo Small100 para traducción offline"""
        model_name = "facebook/mbart-large-50-many-to-many-mmt"
        try:
            self._tokenizer = AutoTokenizer.from_pretrained(model_name)
            self._model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        except Exception as e:
            print(f"Error cargando modelo: {e}")
            raise

    def translate(self, text: str, source: str, target: str) -> str:
        """
        Traduce texto usando el modelo Small100
        
        Args:
            text: Texto a traducir
            source: Código de idioma origen (ej: 'es_ES', 'en_XX')
            target: Código de idioma destino (ej: 'en_XX', 'fr_XX')
        
        Returns:
            Texto traducido
        """
        if not text.strip():
            return ""

        # Mapeo de códigos cortos a códigos Small100
        lang_map = {
            'es': 'es_ES',
            'en': 'en_XX',
            'fr': 'fr_XX',
            'de': 'de_DE',
            'it': 'it_IT',
            'pt': 'pt_XX',
            'ru': 'ru_RU',
            'zh': 'zh_CN',
            'ja': 'ja_XX',
            'ko': 'ko_KR',
            'ar': 'ar_AR',
            'hi': 'hi_IN',
        }

        source_code = lang_map.get(source, source)
        target_code = lang_map.get(target, target)

        # Configurar el tokenizer con el idioma destino
        self._tokenizer.src_lang = source_code
        
        # Tokenizar entrada
        inputs = self._tokenizer(text, return_tensors="pt", padding=True)
        
        # Generar traducción
        with torch.no_grad():
            generated_tokens = self._model.generate(
                **inputs,
                forced_bos_token_id=self._tokenizer.lang_code_to_id[target_code],
                max_length=512,
                num_beams=4,
                early_stopping=True,
            )
        
        # Decodificar resultado
        translation = self._tokenizer.batch_decode(
            generated_tokens, 
            skip_special_tokens=True
        )[0]
        
        return translation