from django.urls import path
from . import views
urlpatterns=[
    path('dis',views.display_std),
    path('add_std',views.add),
    path('edit_std/<id>',views.edit)
]