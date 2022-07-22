from django.shortcuts import render
from django.views import View


class AccountView(View):
    def get(self, request):
        return render(request, "bank_accounts/account.html")

    def post(self, request):
        return render(request, "")
