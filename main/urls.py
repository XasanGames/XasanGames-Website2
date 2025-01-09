from django.urls import path
from . import views

handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
]