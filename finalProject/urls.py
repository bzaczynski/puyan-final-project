from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("bank_auth.urls")),
    path("", include("bank_accounts.urls")),
]
