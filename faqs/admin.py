from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django.db import models

class FAQAdmin(admin.ModelAdmin):
    # Enable CKEditor for answer field (RichTextField)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},  # Enable CKEditor for TextField
    }

    # Custom methods to display translations
    def question_en(self, obj):
        return obj.get_translated('en').get('question', 'No translation')
    
    def answer_en(self, obj):
        return obj.get_translated('en').get('answer', 'No translation')
    
    def question_hi(self, obj):
        return obj.get_translated('hi').get('question', 'No translation')

    def answer_hi(self, obj):
        return obj.get_translated('hi').get('answer', 'No translation')

    # Set sorting for translated fields
    question_en.admin_order_field = 'question_en'  
    answer_en.admin_order_field = 'answer_en'
    question_hi.admin_order_field = 'question_hi'
    answer_hi.admin_order_field = 'answer_hi'

    # Configure which fields to display in the admin panel
    list_display = ('question_en', 'answer_en', 'question_hi', 'answer_hi')
    
    # Allow searching by translated fields (not in list_filter)
    search_fields = ('question_en', 'answer_en', 'question_hi', 'answer_hi')

    # Avoid using custom fields in list_filter
    list_filter = ('question', 'answer')  # Use model fields (not custom methods)

admin.site.register(FAQ, FAQAdmin)
