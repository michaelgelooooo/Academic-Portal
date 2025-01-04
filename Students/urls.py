from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='student-dashboard'),
    path('subjects/', views.subjects, name='student-subjects'),
    path('schedule/', views.schedule, name='student-schedule'),
    path('grades/', views.grades, name='student-grades'),
    path('chat/', views.chat, name='student-chat'),
    path('profile/', views.profile, name='student-profile'),
    path('profile/edit', views.edit_profile, name='student-edit-profile'),
    path('login/', views.login, name='student-login'),
    path('logout/', LogoutView.as_view(next_page='student-login'), name='student-logout'),
]
