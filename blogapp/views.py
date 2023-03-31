from django.forms import SlugField
from django.shortcuts import render, redirect,get_object_or_404
from . models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db.models import Count,Sum
from django . urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# # Create your views here.

# # for user in UserAccount.objects.all():
# #     user.coins_scored -=100
# #     user.save()


def first(request):
    return render(request,'main/home.html')

def home(request):

    return render(request,'main/land.html')


def loginR(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email = email, password = password)

        if user is not None:
            login(request,user)
            messages.success(request,'Logged In Successfully')
            return redirect('notes')

        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'main/land.html')

    else:
        return render(request,'main/land.html')

def registerR(request):


    if request.method == 'POST':

        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')

        if UserAccount.objects.filter(email=email).exists():
            messages.warning(request,'User with this email already exists')
            return render(request,'authentication/register.html')
        else:

            myuser = UserAccount.objects.create_user(email, name, password)
            myuser.save()
            messages.success(request,'User Created Successfully')
            return render(request,'authentication/register.html')

    else:
        return render(request,'authentication/register.html')



def logoutR(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('loginR')



@login_required(login_url='/login/')
def notes(request):
    # notes = (Notes.objects.filter(status = True, typeN= 'Notes') | Notes.objects.filter(status = True, typeN= 'Assignment') | Notes.objects.filter(status = True, typeN= 'Experiment') )

         #Fetches only that notes which are accepted by the admin
    # filteredNotes = NoteFilter(request.GET, queryset = notes)      #Using django-filter extension declared in filters.py file
    # context = {
    #     'notes' : filteredNotes,
    # }
    return render(request,'main/realHome.html')


def dashboard(request):
    return render(request,'main/dashboard.html')









