from spellchecker import SpellChecker


class SpellCheckerService:
    """Servicio de corrección ortográfica similar a DeepL"""
    
    _instances = {}
    
    def __init__(self, language: str = 'es'):
        self.language = language
        if language not in self._instances:
            self._instances[language] = SpellChecker(language)
        self.spell = self._instances[language]
    
    def correct(self, text: str) -> str:
        """
        Corrige errores ortográficos en el texto
        
        Args:
            text: Texto con posibles errores
            
        Returns:
            Texto corregido
        """
        if not text.strip():
            return text
        
        # Dividir el texto en palabras manteniendo puntuación
        words = text.split()
        corrected_words = []
        
        for word in words:
            # Separar puntuación del inicio y final de la palabra
            prefix = ''
            suffix = ''
            clean_word = word
            
            while clean_word and not clean_word[0].isalnum():
                prefix += clean_word[0]
                clean_word = clean_word[1:]
            
            while clean_word and not clean_word[-1].isalnum():
                suffix = clean_word[-1] + suffix
                clean_word = clean_word[:-1]
            
            # Corregir solo si la palabra tiene contenido alfanumérico
            if clean_word:
                # Verificar si está mal escrita
                corrected = self.spell.correction(clean_word.lower())
                
                if corrected:
                    # Mantener mayúsculas si la original las tenía
                    if clean_word[0].isupper():
                        corrected = corrected.capitalize()
                    
                    corrected_words.append(f"{prefix}{corrected}{suffix}")
                else:
                    corrected_words.append(word)
            else:
                corrected_words.append(word)
        
        return ' '.join(corrected_words)
    
    def get_corrections(self, text: str) -> dict:
        """
        Obtiene las correcciones sugeridas para cada palabra mal escrita
        
        Args:
            text: Texto a analizar
            
        Returns:
            Diccionario con palabras incorrectas y sus correcciones
        """
        words = text.split()
        corrections = {}
        
        for word in words:
            clean_word = ''.join(c for c in word if c.isalnum())
            if clean_word and clean_word.lower() not in self.spell.known([clean_word.lower()]):
                candidates = self.spell.candidates(clean_word.lower())
                if candidates:
                    corrections[word] = list(candidates)[:5]  # Máximo 5 sugerencias
        
        return corrections
