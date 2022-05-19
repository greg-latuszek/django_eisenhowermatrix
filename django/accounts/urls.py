from rest_framework.routers import SimpleRouter

from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import QueuedPasswordResetForm

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(form_class=QueuedPasswordResetForm),
        name="password_reset",
    ),
]

# API
router = SimpleRouter()
router.register(r"users", views.UsersViewSet, "users")
