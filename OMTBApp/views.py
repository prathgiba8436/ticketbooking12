from django.shortcuts import render
from OMTBApp.models import Movie,Customer,Admin,Shows
from OMTBApp.forms import MovieForm,CustomerForm,ShowsForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'OMTBApp/index.html')
def addMoive(request):

    if request.method=="POST":
        movieformobj=MovieForm(request.POST,request.FILES)
        if movieformobj.is_valid():
            movieformobj.save()
            return render(request,'OMTBApp/Addmovie.html',{"status":"Movie Added"})
        else:
            return render(request,'OMTBApp/Addmovie.html',{"status":"Movie Not Added"})
    else:
        return render(request,'OMTBApp/AddMovie.html')
#show lis of movies From database
def  movielist(request):
    movielist=Movie.objects.all()
    return render(request,'OMTBApp/movielist.html',{"movielist":movielist})
def DeleteMovie(request,movieId):
    movie=Movie.objects.get(movieId=movieId)
    movie.delete()
    movielist=Movie.objects.all()
    return render(request,'OMTBApp/movielist.html',{"status":"Movie Deleted Successfully","movielist":movielist})
    #after Deleting Movie Get all The Movies and show
def UpdateMovie(request,movieId):
    if request.method=='GET':
        movie=Movie.objects.get(movieId=movieId)
        return render(request,'OMTBApp/updatemovie.html',{'updatemovie':movie})
    elif request.method=='POST':
        movie=Movie.objects.get(movieId=movieId)
        movieformobj=MovieForm(request.POST,request.FILES,instance=movie)
        if movieformobj.is_valid():
            movieformobj.save()
            movielist=Movie.objects.all()
            return render(request,'OMTBApp/movielist.html',{"status":"Movie Updated Successfully","movielist":movielist})
        else:
            return render(request,'OMTBApp/updatemovie.html',{"status":"Movie Not added",'updatemovie':movie})
def SignUp(request):
    if request.method=="GET":
        return render(request,'OMTBApp/AddCustomer.html')
    else:
        customerobj=CustomerForm(request.POST)
        if customerobj.is_valid():
            customerobj.save()
            return render(request,'OMTBApp/AddCustomer.html',{"status":"Customer Added"})
        else:
            return render(request,'OMTBApp/AddCustomer.html',{"status":"Customer Not Added"})
def ShowCustomer(request):
    customerobject=Customer.objects.all()
    return render(request,'OMTBApp/ShowCustomer.html',{'customerobject':customerobject})
def DeleteCustomer(request,CustId):
    customer=Customer.objects.get(CustId=CustId)
    customer.delete()
    customerobject=Customer.objects.all()
    return render(request,'OMTBApp/ShowCustomer.html',{"status":"Customer Deleted Successfully","customerobject":customerobject})
def login(request):
    if request.method=="GET":
        return render(request,'OMTBApp/login.html')
    elif request.method=="POST":
        EmailId=request.POST['EmailId']
        Password=request.POST['Password']
        usertype=request.POST['usertype']
        if usertype=='admin':
            try:
                admin=Admin.objects.get(adminEmailId=EmailId)

                if admin.adminEmailId==EmailId and admin.adminPassword==Password:
                    request.session['admin']=admin.adminEmailId
                    #here we are storing admin objects in session to acess by mulitple request Know as session Tracking
                    return render(request,'OMTBApp/index.html',{'Status':'Admin Login succesfull'})
                else:
                    return render(request,'OMTBApp/login.html',{'Status':'Admin Login Unsuccesfull'})
            except Exception as e:
                return render(request,'OMTBApp/login.html',{'Status':'Admin Login Unsuccesfull'}) 
        elif usertype=='customer':
            try:
                customer=Customer.objects.get(CustEmailId=EmailId)
                if customer.CustEmailId==EmailId and customer.CustPassword==Password:
                    request.session['customer']=customer.CustEmailId
                    return render(request,'OMTBApp/index.html',{'Status':'User Login succesfull'})
                else:
                    return render(request,'OMTBApp/login.html',{'Status':'User Login Unsuccesfull'})
            except Exception as e:
                    return render(request,'OMTBApp/login.html',{'Status':'User Login Unsuccesfull'})
def UpdateCustomer(request,CustId):
    if request.method=='GET':
        customer=Customer.objects.get(CustId=CustId)
        return render(request,'OMTBApp/updatecustomer.html',{'updatecust':customer})
    elif request.method=='POST':
        customer=Customer.objects.get(CustId=CustId)
        customerformobj=CustomerForm(request.POST,instance=customer)
        if customerformobj.is_valid():
            customerformobj.save()
            customerlist=Customer.objects.all()
            return render(request,'OMTBApp/ShowCustomer.html',{"status":"Customer Updated Successfully","customerobject":customerlist})
        else:
            return render(request,'OMTBApp/updatecustomer.html',{"status":"Customer Not added",'updatecust':customer})

def Logout(request):
    session_key=list(request.session.keys())
    for key in session_key:
        del request.session[key]
    return render(request,'OMTBApp/index.html',{'Status':'Logout succesfull'})
def AddShows(request):
    movielist=Movie.objects.all()
    if request.method=='GET':
        return render(request,'OMTBApp/addshows.html',{'movielist':movielist})
    elif request.method=='POST':
        showform=ShowsForm(request.POST)
        if showform.is_valid():
            showform.save()
            return render(request,'OMTBApp/addshows.html',{'movielist':movielist,'status':'Show created Succesfully'})
        else:
            return render(request,'OMTBApp/addshows.html',{'movielist':movielist,'status':'Show Not created'})

def shows(request):
    showobj=Shows.objects.all()
    return render(request,'OMTBApp/showshows.html',{'showobj':showobj})
def updateshow(request,ShowId):
    movielist=Movie.objects.all()
    showobj=Shows.objects.all()

    if request.method=='GET':
        show=Shows.objects.get(ShowId=ShowId)
        return render(request,'OMTBApp/updateshows.html',{'show':show,'movielist':movielist})
    elif request.method=='POST':
        shows=Shows.objects.get(ShowId=ShowId)
        show=ShowsForm(request.POST,instance=shows)
        if show.is_valid():
            show.save()
            showobj=Shows.objects.all()
            return render(request,'OMTBApp/showshows.html',{"status":"Shows Updated Successfully","showobj":showobj})
        else:
            return render(request,'OMTBApp/updateshows.html',{"status":"Shows Not updated",'show':shows,'movielist':movielist})
def deleteshow(request,ShowId):
    show=Shows.objects.get(ShowId=ShowId)
    show.delete()
    showobj=Shows.objects.all()
    return render(request,'OMTBApp/showshows.html',{"status":"Customer Deleted Successfully","showobj":showobj})
def bookShowSeats(request,ShowId):
    if request.method=='GET':
        show=Shows.objects.get(ShowId=ShowId)
        return render(request,'OMTBApp/selectseats.html',{'show':show})