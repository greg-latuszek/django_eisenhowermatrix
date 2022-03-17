from django.urls import path, include

from .views import SignUpView, UsersViewSet
from .forms import QueuedPasswordResetForm
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", UsersViewSet, "users")

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path("password_reset/", auth_views.PasswordResetView.as_view(form_class=QueuedPasswordResetForm),
         name="password_reset"),
    path("api/", include(router.urls)),
]
