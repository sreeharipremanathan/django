from django.urls import path
from . import views
urlpatterns=[
    path('index',views.index_page),
    path('demo',views.demo),
    path('snd',views.second)
]