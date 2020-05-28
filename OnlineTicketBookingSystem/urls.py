"""OnlineTicketBookingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from OMTBApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index),
    path('addmovie',views.addMoive),
    path('movielist',views.movielist),
    path('updatemovie/<int:movieId>',views.UpdateMovie),
    path('deletemovie/<int:movieId>',views.DeleteMovie),
    path('signup',views.SignUp),
    path('showcustomer',views.ShowCustomer),
    path('login',views.login),
    path('deletecustomer/<int:CustId>',views.DeleteCustomer),
    path('updatecust/<int:CustId>',views.UpdateCustomer),
    path('logout',views.Logout),
    path('addshows',views.AddShows),
    path('shows',views.shows),
    path('updateshow/<int:ShowId>',views.updateshow),
    path('deleteshow/<int:ShowId>',views.deleteshow),
    path('bookshow/<int:ShowId>',views.bookShowSeats),



]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)






