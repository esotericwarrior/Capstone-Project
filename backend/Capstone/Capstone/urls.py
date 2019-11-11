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
from iv.views import image_form_upload, video_form_upload, image_favorite, image_delete, image_get_favorites

from django.conf import settings
from django.conf.urls.static import static

# Link to docs which explain adding two-step activation workflow (email verification):
# https://django-registration.readthedocs.io/en/3.0/activation-workflow.html

urlpatterns = [
    # Admin path
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

    # Users API path
    path("api/",
        include("users.api.urls")),

    # Posts paths
    path("api/",
        include("posts.api.urls")),

    # Login via browsable URI
    path("api-auth/",
        include("rest_framework.urls")),

    # Login endpoints via REST
    path("api/rest-auth/",
        include("rest_auth.urls")),

    # Registration endpoint via REST
    path("api/rest-auth/registration/",
        include("rest_auth.registration.urls")),


    path("upload/image/", image_form_upload, name="image"),

    path("upload/video/", video_form_upload, name="video"),

    path("favorite/image/<image_hash>/", image_favorite),

    path("delete/image/<image_hash>/", image_delete),

    path("list/favorites/", image_get_favorites),

    # Catch all for other paths
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
