from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='student-dashboard'),
    path('profile/', views.profile, name='student-profile'),
    path('login/', views.login, name='student-login'),
    path('logout/', LogoutView.as_view(next_page='student-login'), name='student-logout'),
]
