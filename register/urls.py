from django.urls import path
from .views import *

urlpatterns = [
    path("", register, name="register"),
    path("logout/", log_out, name="logout"),
    path("logout/<conf>/", log_out, name="logout_conf")
]