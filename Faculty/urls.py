from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="faculty-dashboard"),
    path("subjects/", views.subjects, name="faculty-subjects"),
    path(
        "subjects/<str:subject_code>", views.subject_view, name="faculty-subject-view"
    ),
    path(
        "subjects/<str:subject_code>/material/upload",
        views.upload_material,
        name="faculty-subjects-material-upload",
    ),
    path(
        "subjects/<str:subject_code>/material/edit/",
        views.edit_material,
        name="faculty-subjects-material-edit",
    ),
    path(
        "subjects/<str:subject_code>/material/delete",
        views.delete_material,
        name="faculty-subjects-material-delete",
    ),
    path("schedule/", views.schedule, name="faculty-schedule"),
    path("advisory/", views.advisory_class, name="faculty-advisory"),
    path("gradebooks/", views.gradebooks, name="faculty-gradebooks"),
    path(
        "gradebooks/<str:subject_code>",
        views.gradebook_view,
        name="faculty-gradebook-view",
    ),
    path(
        "gradebooks/<str:subject_code>/clear-grade/",
        views.clear_grade,
        name="faculty-clear-grade",
    ),
    path("chat/", views.chat, name="faculty-chat"),
    path("profile/", views.profile, name="faculty-profile"),
    path("profile/edit", views.edit_profile, name="faculty-edit-profile"),
    path(
        "profile/update-pic/",
        views.update_profile_pic,
        name="faculty-update-profile-pic",
    ),
    path(
        "profile/update-password/",
        views.update_password,
        name="faculty-update-password",
    ),
    path("login/", views.login, name="faculty-login"),
    path("logout/", views.logout, name="faculty-logout"),
]
