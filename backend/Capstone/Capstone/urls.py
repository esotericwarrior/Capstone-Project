"""Capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

# One-step activation workflow to skip email verification for now:
from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # Registration path
    path("accounts/register/",
        RegistrationView.as_view(
            form_class=CustomUserForm,  # Use CustomUserForm fields in registration form
            success_url="/",    # Route to homepage on successful login
            ), name="django_registration_register"),

    # Remaining URL paths included in django registration package
    path("accounts/",
        include("django_registration.backends.one_step.urls")),

    # Login path (provided by django)
    path("accounts/",
        include("django.contrib.auth.urls")),

    # Login via browsable URI
    path("api-auth/",
        include("rest_framework.urls")),

    # Login endpoints via REST
    path("api/rest-auth/",
        include("rest_auth.urls")),

    # Registration endpoint via REST
    path("api/rest-auth/registration/",
        include("rest_auth.registration.urls")),
]
