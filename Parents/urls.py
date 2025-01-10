from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="parent-dashboard"),
    path("family/", views.family, name="parent-family"),
    path("family/<str:student_id>", views.family_view, name="parent-family-view"),
    path("gradebooks/", views.gradebooks, name="parent-gradebooks"),
    path(
        "gradebooks/<str:student_id>",
        views.gradebook_view,
        name="parent-gradebooks-view",
    ),
    path("announcements/", views.announcements, name="parent-announcements"),
    path("chat/", views.chat, name="parent-chat"),
    path("profile/", views.profile, name="parent-profile"),
    path("profile/edit", views.edit_profile, name="parent-edit-profile"),
    path(
        "profile/update-pic/",
        views.update_profile_pic,
        name="parent-update-profile-pic",
    ),
    path(
        "profile/update-password/", views.update_password, name="parent-update-password"
    ),
    path("login/", views.login, name="parent-login"),
    path("logout/", views.logout, name="parent-logout"),
]
