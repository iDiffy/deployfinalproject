from django.urls import path
from . import views
urlpatterns = [
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("", views.index, name="index"),
    path("home", views.home, name="home"),

    #urls for menu
    path("newmenu",views.newmenu, name="newmenu"),
    path("menu",views.menu,name="menu"),
    path("searchmenu",views.searchmenu,name="searchmenu"),
    path("updatemenu/<str:menucode>",views.updatemenu,name="updatemenu"),
    path("updatemenu/saveupdatemenu/<str:menucode>",views.saveupdatemenu,name="saveupdatemenu"),
    path("deletemenu/<str:menucode>",views.deletemenu,name="deletemenu"),

    #url for customer
    path("newcustomer",views.newcustomer, name="newcustomer"),
    path("searchbymenu",views.searchbymenu, name="searchbymenu")
    ]
