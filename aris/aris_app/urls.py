from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', homepage_views, name = 'homepage_views'),
    # admin templaates url
    path('dashboard/', dashboard_views, name ='dashboard'),
    path('singin/', singin_views, name = 'singin_views'),
    path('singup/', singup_views, name = 'singup_views'),
    path('singout/', singout_view, name = 'singout_view'),
    path('users/', total_users, name = 'total_users'),
    path('add-item/', add_new_item, name = 'add_new_item'),
    path('show-project/', showProject_views, name = 'showProject_views'),
    path('update-item/<int:id>/', updateItem_views, name = 'updateItem_views'),
    path('delete-item/<int:id>/', itemDelete_views, name = 'itemDelete_views'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
