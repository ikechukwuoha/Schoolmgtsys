from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    # Url for the Home page
    path('', views.index, name = 'index'),
    path('examination', views.examination, name = 'examination'),
]