from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='parent-dashboard'),
    path('family/', views.family, name='parent-family'),
    path('chat/', views.chat, name='parent-chat'),
    path('profile/', views.profile, name='parent-profile'),
    path('profile/edit', views.edit_profile, name='parent-edit-profile'),
    path('login/', views.login, name='parent-login'),
    path('logout/', LogoutView.as_view(next_page='parent-login'), name='parent-logout'),
]
