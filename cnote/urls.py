from django.urls import path
from . import views

urlpatterns = [
    path('create-cnote', views.concept_note, name='create-cnote'),
    path('view-cnote', views.view_cnote, name='view-cnote')
]