from django.urls import path
from .views import *

urlpatterns=[
    path('', index) ,
    path('productdetails/<int:product_id>',product_details),
    path('register/',user_register),
    path('login/',user_login),
    path('productlist/',product_list),
    path('logout/',user_logout),
    path('addtocart/<int:product_id>',add_to_cart),
    path('cart/',show_user_cart_items),
    path('removecart/<int:cart_id>',remove_cart),
    path('postorder/<int:product_id>/<int:cart_id>',post_order),
    path('esewaform/',EsewaView.as_view(),name='esewaform'),
    path('esewaverify/<int:order_id>/int:cart_id',esewa_verify),
    path('myorder/',my_order),
    path('profile/',profile),
    path('updateprofile/',update_profile)


]
