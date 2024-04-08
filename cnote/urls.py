from django.urls import path
from . import views

urlpatterns = [
    path('', views.concept_note, name='cnote')
]