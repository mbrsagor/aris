from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    # admin templaates url
    path('dashboard/', Dashboard.as_view(), name ='dashboard')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
