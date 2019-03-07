from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from airbuzz import dummy_data as dummy


def indexView(request):
    if request.user.is_authenticated:
        return dashboardRedirect(request)
    else:
        return render(request, 'index.html')


def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    auth_user = authenticate(request, username=username, password=password)
    if auth_user is not None:
        login(request, auth_user)
        return dashboardRedirect(request)
    else:
        return indexView(request)


def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    fname = request.POST['first_name']
    email = request.POST['email']
    User.objects.create_user(username=username, email=email, password=password, first_name=fname).save()
    auth_user = authenticate(request, username=username, password=password)
    if auth_user is not None:
        login(request, auth_user)
        return dashboardRedirect(request)
    else:
        return indexView(request)


def signout(request):
    logout(request)
    return redirect("/")


@login_required
def dashboardRedirect(request):
    return redirect('/user/' + request.user.username + "/dashboard")


def dashboardView(request, username):
    data = {
        "user": dummy.getUserDummyData()
    }
    return render(request, 'dashboard.html', data)

@login_required
def editProfileView(request, username):
    data = {
        "user": dummy.getUserDummyData(),
    }
    return render(request, 'edit-profile.html', data)
