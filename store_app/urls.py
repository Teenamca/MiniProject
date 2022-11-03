from django.urls import path
from . import views
from store.controller import authview

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name = "collections"),
    path('collections/<str:slug>',views.collectionsview, name = "collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview, name = "productview"),
    path('login/', authview.loginpage, name="login"),
    path('register/',authview.register, name="register" ),
    path('aboutus', views.aboutus, name = "aboutus"),
    path('logout/', authview.logoutpage, name = "logout")
]