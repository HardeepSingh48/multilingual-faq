from django.db import models
from ckeditor.fields import RichTextField

from googletrans import Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Language-specific fields
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def get_translated(self, lang='en'):
        # Generate cache key based on FAQ ID and language
        cache_key = f"faq_{self.id}_lang_{lang}"

        # Check if translation is already cached
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        # If no cached translation, fetch the translation
        translated_question = getattr(self, f'question_{lang}', self.question)
        translated_answer = getattr(self, f'answer_{lang}', self.answer)

        if lang != 'en' and not translated_question:
            # Auto-translate question and answer if not available
            translator = Translator()
            translated_question = translator.translate(self.question, src='en', dest=lang).text
            translated_answer = translator.translate(self.answer, src='en', dest=lang).text

        # Cache the translated result for future use (cache for 1 hour)
        translated_data = {
            'question': translated_question,
            'answer': translated_answer,
        }
        cache.set(cache_key, translated_data, timeout=3600)  # Cache for 1 hour

        return translated_data
