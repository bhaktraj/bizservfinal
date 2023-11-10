from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from database.email import EmailBackend
from database.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render (request, "index.html")
def doLogin(request):
    if request.method == "POST":
       user = EmailBackend.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
       if user!=None:
           login(request,user)
           return redirect('dashboard')
          
       else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('login')
    return render (request, "loginpage.html")
def about(request):
    return render (request, "aboutus.html")
def GeMregistration(request):
    return render (request, "GeM registration.HTML")
def ProductUploading(request):
    return render (request, "Product Uploading.html")
def GeMtrainingCourse(request):
    return render (request, "GeM training Course.html")
def OemAuthorization(request):
    return render (request, "OemAuthorization.html")
def VendorAssessments(request):
    return render (request, "Vendor Assessments.html")
def BidParticipation(request):
    return render (request, "Bid Participation.html")
def TenderNotification(request):
    return render (request, "Tender Notification.html")
def adddetails(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Services = request.POST.get('Services')
        

        details = Query(
            name = name,
            email = email,
            phone = phone,
            Service = Services, )
        
        details.save()
            


        
    return render (request, "thankyou.html")



#dashboard
@login_required(login_url='/login/')
def dashboard(request):
    contact = Query.objects.all().order_by('-id')[:10]
    Pay = Payment.objects.all().order_by('-id')[:10]
    data = {
        'contact':contact,
        'pay':Pay
    }

    return render (request, "dashboard/index.html",data)

def logout_user(request):
    if request.user != None:
        logout(request)
    return redirect("/")