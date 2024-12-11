from django.urls import path
from . import views

urlpatterns=[
    path('',views.shop_login),
    path('logout',views.shop_logout),
    path('register',views.register),

#------------------admin--------------------
    path('shop_home',views.shop_home),
    path('add_pro',views.add_product),
    path('edit_pro/<id>',views.edit_pro),
    path('delete_pro/<id>',views.delete_pro),
    path('bookings',views.bookings),






#-----------------user----------------------
    path('user_home',views.user_home),
    path('view_pro/<id>',views.view_product),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('cart_display',views.cart_display),
    path('delete_cart/<id>',views.delete_cart),
    path('buy_pro/<id>',views.buy_pro),
    path('view_bookings',views.view_bookings)
]