"""Swiggyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.urls import path
from django.views.generic.base import  TemplateView

from ShoppingProject import settings
from shoppingapp import views
from rest_framework.authtoken import views as au


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gen_token/',au.obtain_auth_token),
    path('',TemplateView.as_view(template_name='index.html'),name='home'),

    path('cloths/',views.cloths,name='cloths'),
    path('women_menu/',views.women_menu,name='women_menu'),
    path('shirts/',views.shirts,name='shirts'),
    path('shoe/',views.shoe,name='shoe'),
    path('bags/',views.bags,name='bags'),
    path('kids/',views.kids,name='kids'),
path('boath/',views.boath,name='boath'),
    path('menu/',views.menu,name='menu'),
    path('season_sale/',views.season_sale,name='season_sale'),


     path('watches/',views. watches,name='watches'),
     path('goggules/',views.goggules,name='goggules'),
     path('categires/',views.categires,name='categires'),
     path('formal/',views.formal,name='formal'),
     path('suites/', views.suites, name='suites'),
     path('kurthas/',views.kurthas,name='kurthas'),
     path('tshirts/',views.tshirts,name='tshirts'),
     path('casuals/',views. casuals,name='casuals'),
     path('sarees/',views.sarees,name='sarees'),
     path('l_kurthas/',views.l_kurthas,name='l-kurthas'),
     path('dresses/', views.dresses, name='dresses'),
     path('half_sarees/', views.half_sarees, name='half_sarees'),
     path('kids_half/',views.kids_half,name='kids_half'),
     path('kids_dresses/',views.kids_dresses,name='kids_dresses'),
    path('kids_boys_dresses/',views.kids_boys_dresses,name='kids_boys_dresses'),
    path('clgbags/',views.clgbags,name='clgbags'),
    path('backpack/',views.backpack,name='backpack'),
    path('h_bags/',views.h_bags,name='h_bags'),
    path(
       'formsl_shoes/',views.formsl_shoes,name='formsl_shoes'
    ),
    path('casual_shoes/',views.casual_shoes,name='casual_shoes'),
    path('buy_product/',views.buy_product,name='buy_product'),
    path('buy_add/',views.buy_add,name='buy_add'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('men/',views.men,name='men'),
    path('login_signin/',views.login_signin,name='login_signin'),
    path('signup/',views.signup,name='signup'),
path('logout/',views.logoutt,name='logout'),
    path('add_to_cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
    path('view_cart/',views.view_cart,name='view_cart'),
    path('remove_cart/<int:pk>',views.remove_cart,name='remove_cart'),
    path('checkout/<int:pk>',views.Checkout.as_view(),name='checkout'),
    path('search/',views.search,name='search'),
    path('profile/', views.profile, name='profile'),
    path('orders/', views.orders, name='orders'),
    path('shipping/', views.shipping, name='shipping'),
    path(
       'developer/',views.developer,name='developer'
    ),
    path('deal_day/',views.deal_day,name='deal_day')







]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)