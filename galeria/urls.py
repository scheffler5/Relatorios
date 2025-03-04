from django.urls import path
from galeria.views import index

urlpatterns = [
    path('', index)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
