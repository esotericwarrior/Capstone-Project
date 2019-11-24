from django.urls import include, path
from rest_framework.routers import DefaultRouter

from iv.api import views as ivv

router = DefaultRouter()
router.register(r"iv", ivv.IVViewSet) # Posts endpoint

urlpatterns = [
    path("", include(router.urls)),
]
