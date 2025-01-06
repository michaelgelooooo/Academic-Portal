from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='faculty-dashboard'),
    path('subjects/', views.subjects, name='faculty-subjects'),
    path('subjects/<str:subject_code>', views.subject_view, name='faculty-subject-view'),
    path('schedule/', views.schedule, name='faculty-schedule'),
    path('chat/', views.chat, name='faculty-chat'),
    path('profile/', views.profile, name='faculty-profile'),
    path('profile/edit', views.edit_profile, name='faculty-edit-profile'),
    path('profile/update-pic/', views.update_profile_pic, name='faculty-update-profile-pic'),
    path('profile/update-password/', views.update_password, name='faculty-update-password'),
    path('login/', views.login, name='faculty-login'),
    path('logout/', views.logout, name='faculty-logout'),
]
