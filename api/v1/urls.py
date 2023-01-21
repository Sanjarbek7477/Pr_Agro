from django.urls import path
from api.v1.auth.views import *

urlpatterns = [
    path('auth/', AuthView.as_view())
]
