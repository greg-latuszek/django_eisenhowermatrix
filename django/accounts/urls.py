from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView
from .forms import QueuedPasswordResetForm


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path("password_reset/", auth_views.PasswordResetView.as_view(form_class=QueuedPasswordResetForm),
         name="password_reset"),
]
