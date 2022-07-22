from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from .models import BankUser


class HomeView(View):
    def get(self, request):
        return render(request, "bank_auth/index.html")


class CreateAccountView(View):
    def get(self, request):
        context = {}
        return render(request, "bank_auth/create_account.html", context)

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password_1 = request.POST.get("pass1")
        password_2 = request.POST.get("pass2")

        if password_1 != password_2:
            return redirect("create_account")

        user = BankUser.objects.create(
            first_name=first_name, last_name=last_name, email=email, password=password_1
        )

        user.password = make_password(user.password)
        user.save()

        return render(request, "bank_accounts/account.html")


class LoginView(View):
    def get(self, request):
        context = {}
        return render(request, "bank_auth/login.html", context)

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("pass")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect(reverse("account"))
        return HttpResponse("Something went wrong")
