from django.urls import path
from . import views

handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('contact/', views.contacts, name='contacts'),
    path('privacyPolicy/', views.privacy_policy, name='privacy_policy'),
    path('tos/', views.tos, name='tos'),
]