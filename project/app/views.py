from django.shortcuts import render
from .models import *

def homepage(request):
    return render(request, "app/base.html")

def registerpage(request):
    if request.method == 'POST':
        username = request.POST['name']
        useremail = request.POST['email']
        p1 = request.POST['pass1']
        p2 = request.POST['pass2']

        if p1 == p2 :
            AdminRegister.objects.create(name = username, email = useremail, password = p1)
            return render(request, "app/base.html", {"msgd" : "Now you can Login"} )
        else :
            return render(request, "app/base.html", {"msg" : "Password and Confirm paswword not matched"})
    else :
        return render(request, "app/base.html", {"msg" : "Invalid User"})
    
        
def loginpage(request):
    if request.method == "POST":
        useremail = request.POST['user']
        p1 = request.POST['pass12']

        data = AdminRegister.objects.get(id=1)

        if data.email == useremail and data.password == p1:
            return render(request, "app/Auth/dash.html")
        else :
            return render(request, "app/base.html", { "msgd" : "Username and paswword not matched"})
    else :
        return render(request, "app/base.html", {"msg" : "Invalid User"})
