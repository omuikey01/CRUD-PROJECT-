from django.shortcuts import render
from .models import *
from .forms import *



def homepage(request):
    return render(request, "app/base.html")

def callfunpage(request):
    if request.method == "POST":
        value = request.POST['btn_nav']
        if value == "login":
            return render (request, "app/Auth/login.html")
        

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



def form_showpage(request):
    if request.method == "POST":
        name = request.POST['form_show_admin']
        if name == "add_course" :
            form_couese = CoursesForm()
            return render(request, "app/base.html",{"courses_work" : "add", "add_c" : form_couese})
        
        elif name == "show_course":
            return render(request, "app/base.html",{"courses_work" : "show"})




def courseaddpage(request):
    if request.method == 'POST':

        title = request.POST['title']
        lession = request.POST['lession']
        fees = request.POST['fees']

        Course.objects.create(course_title = title, course_lession = lession, course_fees = fees)
        
        return render(request, "app/base.html",{"msgd" : "Course Successfully Added "})

    else :
        return render(request, "app/base.html", {"msgd" : "Not Added Course"})
        


    