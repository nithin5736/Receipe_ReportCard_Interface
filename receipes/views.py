from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def receipes(request):

    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )

        return redirect("/receipes/")

    queryset = Receipe.objects.all()

    if request.GET.get("search"):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get("search"))

    context = {"receipes": queryset}

    return render(request, "receipe.html", context)


@login_required(login_url="/login")
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipes/")


@login_required(login_url="/login")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        queryset.receipe_name = data.get("receipe_name")
        queryset.receipe_description = data.get("receipe_description")
        if request.FILES.get("receipe_image"):
            queryset.receipe_image = request.FILES.get("receipe_image")
        queryset.save()

        return redirect("/receipes/")

    context = {"receipe": queryset}

    return render(request, "update.html", context)


def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        queryset = User.objects.filter(username=username)

        if not queryset.exists():
            messages.add_message(request, messages.INFO, "Username doesn't exists")
            return redirect("/login")

        user = authenticate(username=username, password=password)
        if user is None:
            messages.add_message(request, messages.INFO, "Invalid password")
            return redirect("/login")
        else:
            login(request, user)
            return redirect("/receipes")

    return render(request, "login.html")


@login_required(login_url="/login")
def logout_page(request):
    logout(request)
    return redirect("/login")


def register(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        queryset = User.objects.filter(username=username)

        if queryset.exists():
            messages.add_message(request, messages.INFO, "Username already exists")
            return redirect("/register")

        user = User.objects.create(username=username)
        user.set_password(password)

        user.save()
        messages.add_message(request, messages.INFO, "Registered successfully")
        return redirect("/register")

    return render(request, "register.html")
