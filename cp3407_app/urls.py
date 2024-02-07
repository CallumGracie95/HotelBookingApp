

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # registration view
    path("users/", include("users.urls")),
    path("dashboard_reporting/", include("dashboard_reporting.urls")),
]
