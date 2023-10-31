from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('u_feedback', views.u_feedback, name="u_feedback"),
]