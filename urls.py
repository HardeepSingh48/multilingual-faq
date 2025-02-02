from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('faqs.urls')),  # Add this line to handle the root path
    path('api/', include('faqs.urls')),
    path('admin/', admin.site.urls),
    # ...existing code...
]
