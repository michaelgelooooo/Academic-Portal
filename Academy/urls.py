from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("administration/support", views.chat, name="admin-support"),
    path("administration/support/conversation/<int:pk>", views.chat_view, name="admin-support-conversation"),
]
