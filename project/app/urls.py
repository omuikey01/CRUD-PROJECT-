from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage),
    path("register/", registerpage, name="regisdata"),
    path("logindata/", loginpage, name="logindata"),

]
