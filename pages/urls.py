from django.urls import path

from .views import HomePageView


urlparttens=[
    path('', HomePageView, name='home')
    ]