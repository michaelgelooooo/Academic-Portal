from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="student-dashboard"),
    path("subjects/", views.subjects, name="student-subjects"),
    path(
        "subjects/<str:subject_code>", views.subject_view, name="student-subject-view"
    ),
    path("schedule/", views.schedule, name="student-schedule"),
    path("grades/", views.grades, name="student-grades"),
    path("announcements/", views.announcements, name="student-announcements"),
    path("chat/", views.chat, name="student-chat"),
    path("chat/view", views.chat_view, name="student-chat-view"),
    path("profile/", views.profile, name="student-profile"),
    path("profile/edit/", views.edit_profile, name="student-edit-profile"),
    path(
        "profile/update-pic/",
        views.update_profile_pic,
        name="student-update-profile-pic",
    ),
    path(
        "profile/update-password/",
        views.update_password,
        name="student-update-password",
    ),
    path("login/", views.login, name="student-login"),
    path("logout/", views.logout, name="student-logout"),
]
