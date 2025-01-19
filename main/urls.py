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
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('base/', views.test, name='test'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
]

