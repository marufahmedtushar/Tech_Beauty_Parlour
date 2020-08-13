from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout , login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import admin_only,allowed_users
from . models import Appointment,Services,AddProduct,AddService,Contact
from math import ceil
from django.core.files.storage import FileSystemStorage

# Create your views here.



@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def index(request):

    appointment = Appointment.objects.all()
    params = {'appointment': appointment}
    return render(request, 'index.html',params)


def registeruser(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user=User.objects.create_user(first_name=first_name,username=username, email=email, password=password)
        group = Group.objects.get(name='customer')
        user.groups.add(group)
        user.save()
        print("created")
        return redirect('/loginuser/')
    else:
        return render(request, 'signup.html')


def about(request):

    return render(request, 'about.html')

@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def users(request):
    user = User.objects.all()
    params = {'user': user}
    return render(request, 'users.html',params)


@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def createuser(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if len(first_name)<4 or len(username)<2 or len(email)<4 or len(password)<4:
            messages.error(request, 'Please fill the form correctly.')
        else:
             user=User.objects.create_user(first_name=first_name,username=username, email=email, password=password)
             group = Group.objects.get(name='customer')
             user.groups.add(group)
             user.save()
             print("created")
    return render(request,'createuser.html')



@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def delete_user(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.delete()
    return redirect("/")


def contact(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        txt = request.POST.get('txt', '')
        if len(first_name) < 4  or len(email) < 4 or len(txt) < 4:
            messages.error(request, 'Please fill the form correctly.')
        else:
            contact = Contact(first_name=first_name, email=email, txt=txt)
            contact.save()
            messages.success(request, 'Your message has been sent.')
    return render(request, 'contact.html')


def services(request):
    services = AddService.objects.all()
    return render(request, 'services.html',{'services':services})


def logintype(request):
    return render(request,'logintype.html')


def loginuser(request):

    """if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)


        if user.groups.filter(name='admin').exists():
                print("execute")
                return render(request, 'userdash.html')


        elif user.groups.filter(name='customer').exists():



             return redirect("/loginuser/")

        elif user is not None:
                            auth.login(request, user)
                            return redirect("/")

    else:
         return render(request, 'login.html')"""


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
                            auth.login(request, user)
                            return redirect("/")

        else:
            return redirect("/loginuser/")

    else:
          return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect("/userdash/")


def userdash(request):
    services =AddService.objects.all()
    n = len(services)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'services': services}
    return render(request, 'userdash.html',params)


@login_required(login_url='/loginuser/')
def appoinment(request):
    services = AddService.objects.all()
    n = len(services)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'services': services}

    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        mobile_number = request.POST.get('mobile_number', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        shedule = request.POST.get('shedule', '')

        if len(first_name)<4 or len(mobile_number)<2 or len(email)<4 or len(address)<4 or len(shedule)<4:
            messages.error(request, 'Please fill the form correctly.')
        else:
            appointment = Appointment(first_name=first_name, mobile_number=mobile_number, email=email, address=address, shedule=shedule)
            appointment.save()

    return render(request,'userdash.html',params)


@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def delete_appointment(request, pk):
    if request.method == 'POST':
        appointment = Appointment.objects.get(pk=pk)
        appointment.delete()
    return redirect("/")


def products(request):
    addproduct = AddProduct.objects.all()
    return render(request,'products.html',{'addproduct': addproduct})

@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def addproduct(request):
    addproduct = AddProduct.objects.all()
    return render(request,'addproduct.html',{'addproduct': addproduct})

@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def uploadprod(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        url = fs.url(filename)
        new_profile = AddProduct(
            name=request.POST['name'],
            image=url
        )
        new_profile.save()
        return redirect('/addproduct/')
    else:
        return redirect('/addproduct/')


@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def addservice(request):
    addservice = AddService.objects.all()
    return render(request,'addservice.html',{'addservice': addservice})


@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def uploadserv(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        url = fs.url(filename)
        new_profile = AddService(
            categories=request.POST['categories'],
            name=request.POST['name'],
            price=request.POST['price'],
            image=url
        )
        new_profile.save()
        return redirect('/addservice/')
    else:
        return redirect('/addservice/')


@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def delete_service(request, pk):
    if request.method == 'POST':
        addservice = AddService.objects.get(pk=pk)
        addservice.delete()
    return redirect("/addservice/")


@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def delete_product(request, pk):
    if request.method == 'POST':
        addproduct = AddProduct.objects.get(pk=pk)
        addproduct.delete()
    return redirect("/addproduct/")


@login_required(login_url='/loginuser/')
@allowed_users(allowed_roles=['admin'])
def makebill(request, id):

        bill = Appointment.objects.filter(pk=id)
        services = Services.objects.all()

        removepunc = request.POST.get('removepunc', 'off')

        if removepunc == "on":
            bill = '''10'''
            newbill = ""
            newbill = newbill + bill
            return render(request, "makebill.html", {'bill': bill[0], 'services': services,'newbill': newbill})

        return render(request,"makebill.html",{'bill': bill[0],'services':services} )


def newbill(request):

    removepunc = request.POST.get('removepunc', 'off')
    newbill = ""

    if removepunc == "on":
        bill = Services.objects.get(id=1)
        bill_result = bill.price

        newbill = newbill + bill_result
        print(bill_result)
    return render(request, "newbill.html", {'new_bill': newbill})