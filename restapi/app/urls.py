from django.urls import path
from . import views


urlpatterns=[
    path('fun1',views.fun1),
    path('fun2',views.fun2),
    path('fun3/<d>',views.fun3),
    path('fun4',views.fun4),
]