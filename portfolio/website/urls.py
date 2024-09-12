from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("resume", views.resume, name="resume"),
    path("bio", views.bio, name="bio"),
]