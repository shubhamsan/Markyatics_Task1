from django.shortcuts import render, HttpResponse, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .models import Reportincident


# Create your views here.
@unauthenticated_user
def index(request):
    return render(request, "markapp/index.html")


@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/userpage')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'markapp/login.html', context)
    # return HttpResponse("this is login page")


def logoutuser(request):
    logout(request)
    return redirect('/login')


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if (request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # this is used for getting the username in views
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('loginuser')

    context = {'form': form}
    return render(request, 'markapp/register.html', context)


@login_required(login_url='/login')
def form(request):
    if request.method == 'POST':
        location = request.POST['location']
        desc = request.POST['desc']
        date = request.POST['date']
        time = request.POST['time']
        inc_location = request.POST['inc_location']
        severety = request.POST['severety']
        cause = request.POST['cause']
        action = request.POST['action']
        environment = request.POST.get('environment')
        injury = request.POST.get('injury')
        damage = request.POST.get('damage')
        vehicle = request.POST.get('vehicle')

        if environment == 'on':
            environment = True
        else:
            environment = False
        if injury == 'on':
            injury = True
        else:
            injury = False
        if damage == 'on':
            damage = True
        else:
            damage = False
        if vehicle == 'on':
            vehicle = True
        else:
            vehicle = False

        details = Reportincident(location=location, desc=desc, date=date, time=time, inc_location=inc_location,
                           severety=severety, cause=cause, action=action, environment=environment, injury=injury,
                           damage=damage, vehicle=vehicle)

        details.save()
        return render(request, 'markapp/form.html')

    return render(request, "markapp/form.html")


@login_required(login_url='/login')
def userpage(request):
    return render(request, "markapp/userpage.html")