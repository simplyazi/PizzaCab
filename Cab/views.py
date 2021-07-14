from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login , logout

from django.contrib import messages

from .forms import CreateUserForm

# Create your views here.
def home(request):
    return render(request,'HomePage.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '  + user)


            return redirect('login')

    context = {'form':form}
    return render (request, 'Accounts/register.html',context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            return redirect('home')
        else:
            messages.info(request,'Username OR Password is INCORRECT')

    context = {}
    return render (request, 'Accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
