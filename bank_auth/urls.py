from django.urls import path

from .views import CreateAccountView, HomeView, LoginView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("create_account/", CreateAccountView.as_view(), name="create_account"),
]
