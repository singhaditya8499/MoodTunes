from django.urls import path
from . import views

urlpatterns = [
    path('', views.ham_a_questionnaire, name='questionnaire'),
]
