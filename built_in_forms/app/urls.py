from django.urls import path
from . import views

urlpatterns=[
    path('',views.normal_form_fun),
    path('model_form',views.model_form_fun),
]