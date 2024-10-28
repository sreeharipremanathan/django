from django.urls import path
from . import views
urlpatterns=[
    path('dis',views.display),
    # path('std',views.std_dtls),
    path('edit/<id>',views.edit),
    path('dlt/<id>',views.delete)
]