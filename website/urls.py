from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('wishlist.html', views.wishlist, name="wishlist"),
    path('product_detail.html', views.product_detail, name="product-detail"),
    path('product_list.html', views.product_list, name="product-list"),
    path('my_account.html', views.my_account, name="my-account"),
    path('login.html', views.login, name="login"),
    path('checkout.html', views.checkout, name="checkout"),
    path('cart.html', views.cart, name="cart"),
]
