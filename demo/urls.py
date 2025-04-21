
from django.urls import path 
from . import views

from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.productView.as_view(), name='home'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),

    path('details/<int:id>/', views.ProductDetails.as_view(), name='details'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html',  authentication_form=LoginForm),name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
     path('profile/', views.profile, name='profile'),
    path('mens/',views.mens, name='mens'),
    path('search/',views.search, name='search'),
     path('add-to-carts/', views.addToCart, name="addCart"),

    path('shoes/',views.shoes,name='shoes'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('cart/', views.cart, name="cart"),
    path('women/',views.women,name='women'),
    path('sunglasses/',views.sunglasses,name='sunglasses'),
    path('camera/',views.camera,name='camera'),
]