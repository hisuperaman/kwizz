from django.urls import path, include
from . import views

app_name = "home"
urlpatterns = [
    path("", view=views.index, name="index"),

    path("getHostQuizHeldStatus/", view=views.getHostQuizHeldStatus, name="getHostQuizHeldStatus")
]