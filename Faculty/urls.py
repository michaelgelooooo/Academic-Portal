from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='faculty-dashboard'),
    path('schedule/', views.schedule, name='faculty-schedule'),
    path('chat/', views.chat, name='faculty-chat'),
    path('profile/', views.profile, name='faculty-profile'),
    path('profile/edit', views.edit_profile, name='faculty-edit-profile'),
    path('profile/update-pic/', views.update_profile_pic, name='faculty-update-profile-pic'),
    path('login/', views.login, name='faculty-login'),
    path('logout/', LogoutView.as_view(next_page='faculty-login'), name='faculty-logout'),
]
