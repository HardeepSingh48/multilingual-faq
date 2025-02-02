from django.urls import path
from .views import FAQListView

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faq_list'),
    path('', faq_list, name='faq-list'),
]