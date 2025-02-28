from django.shortcuts import render,redirect
from hospitalapp.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def departments(request):
    return render(request,'departments.html')

def doctors(request):
    return render(request,'doctors.html')

def appointment(request):
    if request.method == "POST":
        myappointment =Appointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message']
        )

        myappointment.save()
        return redirect('/appointment')

    else:
        return render(request,'appointment.html')

def contact(request):
    if request.method == "POST":
        mycontact =Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )

        mycontact.save()
        return redirect('/contact')

    else:
        return render(request,'contact.html')
