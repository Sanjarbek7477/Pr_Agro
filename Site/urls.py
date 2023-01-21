from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home_page'),
    path('add/', add, name='add'),
    path('advert/', advert, name='advert'),
    path('form/', form, name='form'),
    path('page/', page, name='page'),
    path('payment/', payment, name='payment'),
    path('razdel/', razdel, name='razdel'),
]
