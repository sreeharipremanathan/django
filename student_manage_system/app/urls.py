from django.urls import path
from . import views
urlpatterns=[
    path('dis',views.display_std)
]