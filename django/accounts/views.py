from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets
from django.contrib.auth.models import User
from .forms import NewUserForm
from .serializers import UserSerializer


class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# DRF
class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
