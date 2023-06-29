import adminapp.views
from django.shortcuts import render , redirect
from adminapp import views
import requests
from .models import appointmenttable
from .models import commenttable
from .models import contacttable
from .models import registertable
from django.contrib import messages

# Create your views here.

def indexone(request):
    return render(request,'index.html')

def dashlogin(request):
    return render(request,'index2.html')

def plogin(request):
    return render(request,'patient.html')

def about(request):
    return render(request,'about.html')

def doctor(request):
    return render(request,'doctors.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def bdetails(request):
    return render(request,'blog-details.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def ecg(request):
    return render(request,'ecg.html')

def pulse(request):
    return render(request,'pulse.html')

def temp(request):
    return render(request,'temp.html')

def appointment(request):
    if request.method == 'POST':
        Name = request.POST.get("name")
        Email = request.POST.get("eaddress")
        Date = request.POST.get("date")
        Departement = request.POST.get("departement")
        Number = request.POST.get("number")
        Message = request.POST.get("message")

        query = appointmenttable(Name=Name,Email=Email,Date=Date,Departement=Departement,Number=Number,Message=Message)
        query.save()
    else:
        pass

    return render(request,'index.html')

def comment(request):
    if request.method == 'POST':
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Website = request.POST.get("website")
        Message = request.POST.get("msg")

        query = commenttable(Name=Name,Email=Email,Website=Website,Message=Message)
        query.save()
    else:
        pass

    return render(request,'index.html')


def contactt(request):
    if request.method == 'POST':
        Name = request.POST.get("fname")
        Email = request.POST.get("emailaddress")
        Subject = request.POST.get("subject")
        Message = request.POST.get("message")

        query = contacttable(Name=Name,Email=Email,Subject=Subject,Message=Message)
        query.save()
    else:
        pass

    return render(request,'index.html')

def registerdata(request):
    if request.method == 'POST':
        Name = request.POST.get("fname")
        Email = request.POST.get("email")
        Number = request.POST.get("number")
        Password = request.POST.get("password")
        Address = request.POST.get("address")



        try:
            validateuser = registertable.objects.get(Email=Email)
        except:
            validateuser = None

        if validateuser is None:
            query = registertable(Name=Name,Email=Email,Number=Number,Password=Password,Address=Address,role=2)
            query.save()
        else:
            messages.error(request,"You Are Already Registered. Please Login")
            return render(request,"register.html")

    else:
        pass
    return render(request,'index.html')

def logindata(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        userpassword = request.POST.get("password")

        try:
            checkuser = registertable.objects.get(Email=username,Password=userpassword)
            request.session['logid'] = checkuser.id
            request.session['logname'] = checkuser.Name
            request.session['logrole'] = checkuser.role
            request.session.save()
        except:
            checkuser = None


        if checkuser is not None:
            if checkuser.role == 1:
                return redirect(adminapp.views.index)
            else:
                return redirect(adminapp.views.patient)
        else:
            messages.error(request,'Wrong Username Or Password !!!')
            return redirect(login)

    else:
        pass

    return redirect(login)

def dashboardpage(request):
    return render(request,'session.html')

def logout(request):
    try:
        del request.session['logid']
        del request.session['logname']
    except:
        pass
    return render(request,'login.html')

