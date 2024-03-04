from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage),
    path("callfun/", callfunpage, name="callfun"),
    path("register/", registerpage, name="regisdata"),
    path("logindata/", loginpage, name="logindata"),
    path("courseadd/", courseaddpage, name="courseadd"),
    path("form_show/", form_showpage, name="form_show"),

    

]
