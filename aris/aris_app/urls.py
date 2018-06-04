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
    path('blood-doner/', bloodDonorList_views, name = 'bloodDonorList_views'),
    path('doner-remove/<int:id>/', bloodDonorRemove, name = 'bloodDonorRemove'),
    path('about/', aboutus_views, name ='aboutUsViews'),
    path('dashboard/update-about/<int:id>/', updateAbout_views, name = 'updateAbout_views'),
    path('add-service/', serverSection_views, name = 'serverSection_views'),
    path('dashboard/all-services/', allService_views, name = 'allService_views'),
    path('delete-services/<int:id>/', deleteService_views, name = 'deleteService_views'),
    path('dashboard/updateservice/<int:id>/', updateService_views, name = 'updateService_views'),
    path('add-portfolio/', portfolio_views, name = 'portfolio_views'),
    path('all-portfolio/', allportfolio_views, name = 'allportfolio_views'),
    path('dashboard/update-portfolio/<int:id>/', updatePportoflio, name = 'updatePportoflio'),
    path('dashboard/delete-portfolio/<int:id>/', deletePortfolio, name = 'deletePortfolio'),
    path('add-member/', teamMember_views, name = 'teamMember_views'),
    path('all-member/', listOfAllMemeber_views, name = 'listOfAllMemeber_views'),
    path('dashboard/update-memeber/<int:id>/', updateTeamMember, name = 'updateTeamMember'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
