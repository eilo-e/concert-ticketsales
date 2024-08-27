from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
import ticketsale
import ticketsale.views



def loginview(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
    
    if user is not None:
        login(request,user)
        if request.GET.get('next'):
         return HttpResponseRedirect(request.GET.get('next'))
        
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
       
    else:
            context={
            "username":username,
            "کاربری با این مشخصات یافت نشد":"errorMessage"
            }
            return render(request, "accounts/login.html", context)
    

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(ticketsale.views.concertListView))

#else:
#sreturn render(request, "accounts/login.html", {})
