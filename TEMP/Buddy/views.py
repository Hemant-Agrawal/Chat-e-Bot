from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from . import models

from .logics import logic, Queries, temp

chat = logic.Chat(Queries.pairs, logic.reflections)


def get_response(request):
    message = request.GET['msg']
    response = chat.converse(message)
    if "Sorry" in response or "Please" in response or len(response) < 3:
        query = models.Queries(query=message, response=response, user=request.user)
        query.save()
    return JsonResponse({'response': response})


def live_response(request):
    message = request.GET['msg']
    response = client.send_message(message)
    return JsonResponse({'response': response})


def login(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/ChatBot")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("/login")

    else:
        return render(request, "registration/user.html", {"login": "checked", "signup": "", "error": ""})


def register(request):
    if request.method == "POST":
        first_name = request.POST['First_Name']
        last_name = request.POST['Last_Name']
        username = request.POST['Username']
        email = request.POST['Email']
        password = request.POST['Password']
        confirm = request.POST['Confirm']

        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already taken")
                print("Username Already taken")
                return redirect("/register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already taken")
                print("Username Already taken")
                return redirect("/register")
            else:
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)
                user.save()
                return redirect("/login")
        else:
            return redirect("/register")
    else:
        return render(request, "registration/user.html", {"signup": "checked", "login": ""})


def logout(request):
    auth.logout(request)
    return redirect("/")


def Homepage(request):
    return render(request, "HomePage.html")


def ChatBot(request):
    if request.user.is_authenticated:
        return render(request, "ChatBot.html")
    else:
        return redirect("/login")


def temp(request):
    return render(request, "temp.html")


def ChatRoom(request):
    return render(request, "ChatRoom.html")
