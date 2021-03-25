from django.urls import path
from . import views

urlpatterns = [
    path('license-keys-generator/', views.apiOverview, name='api-overview'),

    # License Key Generator URLs

    path('license-keys-list/', views.licenseKeyList, name='license-keys-list'),
    path('license-keys-detail/<str:pk>/', views.licenseKeyDetail, name='license-keys-detail'),
    path('license-keys-generate/', views.licenseKeyGenerate, name='license-keys-generate'),
    path('license-keys-delete/<str:pk>/', views.licenseKeyDelete, name='license-keys-delete'),

]
