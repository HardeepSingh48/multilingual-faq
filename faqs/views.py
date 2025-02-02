from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')  # Default to English
        faqs = FAQ.objects.all()

        # Convert each FAQ into translated format
        translated_faqs = [faq.get_translated(lang) for faq in faqs]

        # Structured response for better readability
        response_data = {
            "status": "success",
            "language": lang,
            "total_faqs": len(translated_faqs),
            "faqs": translated_faqs
        }

        return Response(response_data)
